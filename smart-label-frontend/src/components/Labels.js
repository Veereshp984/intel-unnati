import React, { useState } from "react";
import { createLabel, autoGenerateLabels, printLabel, verifyLabel } from "../api/api";
import { Typography, List, ListItem, ListItemText, Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions, Checkbox, FormControlLabel, CircularProgress, Stack, Grid, Card, CardContent, CardActions, Divider } from "@mui/material";
import { useSnackbar } from "./SnackbarProvider";
import PrintIcon from '@mui/icons-material/Print';
import VerifiedIcon from '@mui/icons-material/Verified';
import LabelImportantIcon from '@mui/icons-material/LabelImportant';
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

function Labels({ productId, labels, refresh, product }) {
  const [open, setOpen] = useState(false);
  const [form, setForm] = useState({ label_type: "qr_code", label_data: "", auto_generate: false });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [autoLoading, setAutoLoading] = useState(false);
  const [printLoading, setPrintLoading] = useState("");
  const [verifyLoading, setVerifyLoading] = useState("");
  const showSnackbar = useSnackbar();
  const [imgUrls, setImgUrls] = useState({});
  const [printDivId, setPrintDivId] = useState(null);

  // Fetch label images when labels change
  React.useEffect(() => {
    const fetchImages = async () => {
      const urls = {};
      for (const label of labels) {
        if (label.has_image) {
          try {
            urls[label.id] = `${process.env.REACT_APP_API_BASE || 'http://localhost:5000/api'}/labels/${label.id}/image?${Date.now()}`;
          } catch {}
        }
      }
      setImgUrls(urls);
    };
    fetchImages();
  }, [labels]);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = e => {
    e.preventDefault();
    setLoading(true);
    setError("");
    createLabel(productId, form)
      .then(() => {
        setOpen(false);
        setForm({ label_type: "qr_code", label_data: "", auto_generate: false });
        refresh();
        showSnackbar("Label created successfully!", "success");
      })
      .catch(err => {
        setError(err.response?.data?.error || "Error creating label");
        showSnackbar(err.response?.data?.error || "Error creating label", "error");
      })
      .finally(() => setLoading(false));
  };

  const handleAuto = () => {
    setAutoLoading(true);
    autoGenerateLabels(productId)
      .then(() => {
        refresh();
        showSnackbar("Label auto-generated successfully!", "success");
      })
      .catch(err => {
        showSnackbar(err.response?.data?.error || "Error auto-generating label", "error");
      })
      .finally(() => setAutoLoading(false));
  };

  const handlePrint = (labelId) => {
    setPrintLoading(labelId);
    printLabel(labelId)
      .then(() => {
        setTimeout(refresh, 3000);
        showSnackbar("Print job started!", "info");
      })
      .catch(err => {
        showSnackbar(err.response?.data?.error || "Error printing label", "error");
      })
      .finally(() => setPrintLoading(""));
  };

  const handleVerify = (labelId) => {
    setVerifyLoading(labelId);
    verifyLabel(labelId)
      .then(() => {
        refresh();
        showSnackbar("Label verified!", "success");
      })
      .catch(err => {
        showSnackbar(err.response?.data?.error || "Error verifying label", "error");
      })
      .finally(() => setVerifyLoading(""));
  };

  // Download QR code image
  const handleDownload = (labelId) => {
    const url = imgUrls[labelId];
    if (url) {
      const link = document.createElement('a');
      link.href = url;
      link.download = `qr_code_${labelId}.png`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  // Print label details as text-only PDF (robust)
  const handlePrintPDF = (label) => {
    const pdf = new jsPDF({ orientation: 'portrait', unit: 'pt', format: 'a4' });
    let y = 40;
    pdf.setFontSize(14);
    pdf.text(`Product Name: ${product?.name || ''}`, 40, y); y += 24;
    pdf.text(`Batch Number: ${product?.batch_number || ''}`, 40, y); y += 24;
    pdf.text(`Manufacturing Date: ${product?.manufacturing_date || ''}`, 40, y); y += 24;
    pdf.text(`Expiry Date: ${product?.expiry_date || ''}`, 40, y); y += 24;
    pdf.text(`Print Status: ${label.print_status === 'printed' ? 'Yes' : 'No'}`, 40, y); y += 24;
    pdf.text(`Label Type: ${label.label_type} (${label.auto_generated ? 'Auto' : 'Manual'})`, 40, y); y += 24;
    pdf.text(`Verified: Yes`, 40, y);
    pdf.save(`label_details_${label.id}.pdf`);
  };

  // Print QR code and details using browser print dialog (robust)
  const handlePrintLabel = (labelId) => {
    const printArea = document.getElementById(`print-area-${labelId}`);
    if (!printArea) {
      showSnackbar('Print area not found. Please try again or refresh the page.', 'error');
      alert('Print area not found. Please try again or refresh the page.');
      return;
    }
    const printContents = printArea.innerHTML;
    let printWindow = null;
    try {
      printWindow = window.open('', '', 'height=600,width=400');
      if (!printWindow) {
        showSnackbar('Popup blocked! Please allow popups for this site to print.', 'error');
        alert('Popup blocked! Please allow popups for this site to print.');
        return;
      }
      printWindow.document.write('<html><head><title>Print Label</title>');
      printWindow.document.write('</head><body >');
      printWindow.document.write(printContents);
      printWindow.document.write('</body></html>');
      printWindow.document.close();
      printWindow.focus();
      showSnackbar('Print dialog opened. Please select your printer.', 'info');
      printWindow.print();
      printWindow.close();
    } catch (e) {
      showSnackbar('Error opening print dialog. ' + e.message, 'error');
      alert('Error opening print dialog. ' + e.message);
      if (printWindow) printWindow.close();
    }
  };

  return (
    <div>
      <Typography variant="h6" gutterBottom>Labels</Typography>
      <Stack direction="row" spacing={2} mb={2}>
        <Button variant="contained" color="primary" onClick={() => setOpen(true)} disabled={loading}>
          {loading ? <CircularProgress size={20} color="inherit" /> : "Add Label"}
        </Button>
        <Button variant="outlined" color="secondary" onClick={handleAuto} disabled={autoLoading}>
          {autoLoading ? <CircularProgress size={20} color="inherit" /> : "Auto Generate Label"}
        </Button>
      </Stack>
      <Divider />
      <Grid container spacing={2}>
        {labels.map((label, idx) => (
          <Grid item xs={12} sm={6} md={4} key={idx}>
            <Card elevation={2} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 6 } }}>
              <CardContent>
                {/* QR Code Image Display */}
                {label.has_image && imgUrls[label.id] && (
                  <div id={`print-area-${label.id}`} style={{ textAlign: 'center', marginBottom: 8 }}>
                    <img
                      src={imgUrls[label.id]}
                      alt="QR Code"
                      style={{ maxWidth: '100%', maxHeight: 180, border: '1px solid #eee', borderRadius: 8 }}
                    />
                    <Typography variant="caption" color="textSecondary">Right-click to save or scan</Typography>
                    <Stack direction="row" spacing={1} justifyContent="center" mt={1}>
                      <Button size="small" variant="outlined" onClick={() => handleDownload(label.id)}>
                        Download PDF
                      </Button>
                      <Button size="small" variant="outlined" color="secondary" onClick={() => handlePrintPDF(label)}>
                        Download Details PDF
                      </Button>
                    </Stack>
                  </div>
                )}
                {/* Hidden PDF area for label details only */}
                <div id={`pdf-area-${label.id}`} style={{ display: 'none' }}>
                  <div><b>Product Name:</b> {product?.name || ''}</div>
                  <div><b>Batch Number:</b> {product?.batch_number || ''}</div>
                  <div><b>Manufacturing Date:</b> {product?.manufacturing_date || ''}</div>
                  <div><b>Expiry Date:</b> {product?.expiry_date || ''}</div>
                  <div><b>Print Status:</b> {label.print_status === 'printed' ? 'Yes' : 'No'}</div>
                  <div><b>Label Type:</b> {label.label_type} ({label.auto_generated ? "Auto" : "Manual"})</div>
                </div>
                {/* Show product details on the visible label card */}
                <Stack direction="row" alignItems="center" spacing={1} mb={1}>
                  <LabelImportantIcon color={label.auto_generated ? "secondary" : "primary"} />
                  <Typography variant="subtitle1">{label.label_type} ({label.auto_generated ? "Auto" : "Manual"})</Typography>
                </Stack>
                {/* Removed: Data (URL), Print Status, Verified */}
              </CardContent>
              <CardActions>
                <Button
                  variant="outlined"
                  color="primary"
                  size="small"
                  startIcon={<PrintIcon />}
                  onClick={() => handlePrint(label.id)}
                  disabled={label.print_status === "printed" || !!printLoading}
                  style={{ marginRight: 8 }}
                >
                  {printLoading === label.id ? <CircularProgress size={18} color="inherit" /> : "Print"}
                </Button>
                <Button
                  variant="outlined"
                  color="success"
                  size="small"
                  startIcon={<VerifiedIcon />}
                  onClick={() => handleVerify(label.id)}
                  disabled={label.is_verified || !!verifyLoading}
                >
                  {verifyLoading === label.id ? <CircularProgress size={18} color="inherit" /> : "Verify"}
                </Button>
              </CardActions>
            </Card>
          </Grid>
        ))}
      </Grid>
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>Add Label</DialogTitle>
        <form onSubmit={handleSubmit}>
          <DialogContent>
            <TextField label="Label Type" name="label_type" value={form.label_type} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Label Data" name="label_data" value={form.label_data} onChange={handleChange} fullWidth margin="normal" />
            <FormControlLabel
              control={
                <Checkbox
                  checked={form.auto_generate}
                  onChange={e => setForm({ ...form, auto_generate: e.target.checked })}
                  name="auto_generate"
                  color="primary"
                />
              }
              label="Auto Generate"
            />
            {error && <Typography color="error">{error}</Typography>}
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" color="primary" disabled={loading}>
              {loading ? <CircularProgress size={20} color="inherit" /> : "Add"}
            </Button>
          </DialogActions>
        </form>
      </Dialog>
    </div>
  );
}
export default Labels;
