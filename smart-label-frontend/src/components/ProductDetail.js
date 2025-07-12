import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getProduct, updateProduct, deleteProduct, runProductWorkflow, clearAutoQualityChecks, clearAutoLabels } from "../api/api";
import { Container, Typography, CircularProgress, Paper, Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle, List, ListItem, ListItemText, Box, Alert } from "@mui/material";
import Grid from '@mui/material/Grid';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Divider from '@mui/material/Divider';
import QualityChecks from "./QualityChecks";
import Labels from "./Labels";

function ProductDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [editOpen, setEditOpen] = useState(false);
  const [editForm, setEditForm] = useState({});
  const [error, setError] = useState("");
  const [workflowLoading, setWorkflowLoading] = useState(false);
  const [workflowMsg, setWorkflowMsg] = useState("");

  useEffect(() => {
    getProduct(id)
      .then(res => {
        setProduct(res.data.product);
        setEditForm(res.data.product);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [id]);

  const handleEditChange = e => {
    setEditForm({ ...editForm, [e.target.name]: e.target.value });
  };

  const handleEditSubmit = e => {
    e.preventDefault();
    updateProduct(id, editForm)
      .then(res => {
        setProduct(res.data.product);
        setEditOpen(false);
      })
      .catch(err => setError(err.response?.data?.error || "Error updating product"));
  };

  const handleDelete = () => {
    if (window.confirm("Are you sure you want to delete this product?")) {
      deleteProduct(id).then(() => navigate("/"));
    }
  };

  const handleRunWorkflow = () => {
    setWorkflowLoading(true);
    setWorkflowMsg("");
    runProductWorkflow(product.id)
      .then(res => {
        setWorkflowMsg(res.data.message);
        setWorkflowLoading(false);
        setTimeout(() => {
          getProduct(id).then(res => setProduct(res.data.product));
        }, 2000);
      })
      .catch(err => {
        setWorkflowMsg(err.response?.data?.error || "Error running workflow");
        setWorkflowLoading(false);
      });
  };

  if (loading) return <CircularProgress />;
  if (!product) return <Typography>Product not found.</Typography>;

  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mb: 3, animation: 'fadeInDown 0.8s' }}>{product.name}</Typography>
      {/* Show product quality status */}
      {product.quality_status && (
        <Alert severity={product.is_good ? "success" : "error"} sx={{ mb: 2 }}>
          {product.quality_status}
        </Alert>
      )}
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card elevation={8} sx={{ mb: 2, borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)', backdropFilter: 'blur(8px)', animation: 'fadeInUp 1s' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>Product Information</Typography>
              <Divider sx={{ mb: 2 }} />
              <Typography><b>Category:</b> {product.category}</Typography>
              <Typography><b>Description:</b> {product.description}</Typography>
              <Typography><b>Manufacturer:</b> {product.manufacturer}</Typography>
              <Typography><b>Batch Number:</b> {product.batch_number}</Typography>
              <Typography><b>Manufacturing Date:</b> {product.manufacturing_date}</Typography>
              <Typography><b>Expiry Date:</b> {product.expiry_date}</Typography>
              <Typography><b>Status:</b> {product.workflow_status}</Typography>
            </CardContent>
          </Card>
          <Card elevation={8} sx={{ mb: 2, borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)', backdropFilter: 'blur(8px)', p: 2, animation: 'fadeInUp 1.1s' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>Actions</Typography>
              <Divider sx={{ mb: 2 }} />
              <Grid container spacing={1}>
                <Grid item xs={12} sm={6}>
                  <Button
                    variant="outlined"
                    color="warning"
                    fullWidth
                    sx={{ mb: 1, fontWeight: 700, borderRadius: 2, borderWidth: 2, borderColor: 'warning.main', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #ff9800 0%, #ff80ab 100%)', color: '#fff', borderColor: 'warning.main', boxShadow: '0 8px 32px 0 #ff980044' } }}
                    onClick={() => {
                      if (window.confirm("Are you sure you want to clear all auto-generated quality checks?")) {
                        clearAutoQualityChecks(product.id).then(() => getProduct(id).then(res => setProduct(res.data.product)));
                      }
                    }}
                  >
                    Clear Auto Quality Checks
                  </Button>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Button
                    variant="outlined"
                    color="warning"
                    fullWidth
                    sx={{ mb: 1, fontWeight: 700, borderRadius: 2, borderWidth: 2, borderColor: 'warning.main', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #ff9800 0%, #ff80ab 100%)', color: '#fff', borderColor: 'warning.main', boxShadow: '0 8px 32px 0 #ff980044' } }}
                    onClick={() => {
                      if (window.confirm("Are you sure you want to clear all auto-generated labels?")) {
                        clearAutoLabels(product.id).then(() => getProduct(id).then(res => setProduct(res.data.product)));
                      }
                    }}
                  >
                    Clear Auto Labels
                  </Button>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Button variant="contained" color="primary" fullWidth sx={{ mb: 1, fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #1976d244', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #1976d244' } }} onClick={() => setEditOpen(true)}>
                    Edit
                  </Button>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Button variant="contained" color="secondary" fullWidth sx={{ mb: 1, fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #ff80ab44', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #ff80ab 0%, #ff9800 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #ff80ab44' } }} onClick={handleDelete}>
                    Delete
                  </Button>
                </Grid>
                <Grid item xs={12}>
                  <Button
                    variant="contained"
                    color="primary"
                    fullWidth
                    sx={{ mb: 1, fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #1976d244', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #1976d244' } }}
                    onClick={handleRunWorkflow}
                    disabled={workflowLoading}
                  >
                    Run Workflow Automation
                  </Button>
                  {workflowLoading && <CircularProgress size={24} sx={{ ml: 2, verticalAlign: "middle" }} />}
                  {workflowMsg && <Typography color="secondary" sx={{ mt: 1, fontWeight: 600, animation: 'fadeIn 1s' }}>{workflowMsg}</Typography>}
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <Card elevation={8} sx={{ mb: 2, borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)', backdropFilter: 'blur(8px)', animation: 'fadeInUp 1.2s' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>Quality Checks</Typography>
              <Divider sx={{ mb: 2 }} />
              <QualityChecks
                productId={product.id}
                productName={product.name}
                qualityChecks={product.quality_checks || []}
                refresh={() => {
                  getProduct(id).then(res => setProduct(res.data.product));
                }}
              />
            </CardContent>
          </Card>
          <Card elevation={8} sx={{ mb: 2, borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)', backdropFilter: 'blur(8px)', animation: 'fadeInUp 1.3s' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>Labels</Typography>
              <Divider sx={{ mb: 2 }} />
              <Labels
                productId={product.id}
                labels={product.labels || []}
                refresh={() => {
                  getProduct(id).then(res => setProduct(res.data.product));
                }}
                product={product}
              />
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12}>
          <Card elevation={8} sx={{ mb: 2, borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)', backdropFilter: 'blur(8px)', animation: 'fadeInUp 1.4s' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>Workflow Logs</Typography>
              <Divider sx={{ mb: 2 }} />
              <List>
                {(product.workflow_logs || []).map((log, idx) => (
                  <ListItem key={idx} sx={{ borderBottom: '1px solid #eee', animation: `fadeIn 0.7s ${0.1 * idx}s` }}>
                    <ListItemText
                      primary={<span style={{ fontWeight: 600 }}>{`${log.action} (${log.status})`}</span>}
                      secondary={log.details}
                    />
                  </ListItem>
                ))}
                {(!product.workflow_logs || product.workflow_logs.length === 0) && (
                  <Typography color="text.secondary" align="center">No workflow logs available.</Typography>
                )}
              </List>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
      <Dialog open={editOpen} onClose={() => setEditOpen(false)}>
        <DialogTitle>Edit Product</DialogTitle>
        <form onSubmit={handleEditSubmit}>
          <DialogContent sx={{ background: 'rgba(255,255,255,0.95)', borderRadius: 2, boxShadow: '0 4px 24px 0 #1976d244', animation: 'fadeInDown 0.7s' }}>
            <TextField label="Name" name="name" value={editForm.name || ""} onChange={handleEditChange} fullWidth required margin="normal" />
            <TextField label="Description" name="description" value={editForm.description || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Category" name="category" value={editForm.category || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Manufacturer" name="manufacturer" value={editForm.manufacturer || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Batch Number" name="batch_number" value={editForm.batch_number || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Manufacturing Date" name="manufacturing_date" type="date" value={editForm.manufacturing_date ? editForm.manufacturing_date.substring(0,10) : ""} onChange={handleEditChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
            <TextField label="Expiry Date" name="expiry_date" type="date" value={editForm.expiry_date ? editForm.expiry_date.substring(0,10) : ""} onChange={handleEditChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
            {error && <Typography color="error">{error}</Typography>}
          </DialogContent>
          <DialogActions sx={{ background: 'rgba(255,255,255,0.95)', borderRadius: 2, boxShadow: '0 4px 24px 0 #1976d244' }}>
            <Button onClick={() => setEditOpen(false)} sx={{ fontWeight: 600 }}>Cancel</Button>
            <Button type="submit" variant="contained" color="primary" sx={{ fontWeight: 700, boxShadow: '0 2px 8px 0 #1976d244', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', color: '#fff' } }}>Save</Button>
          </DialogActions>
        </form>
      </Dialog>
    </Container>
  );
}
export default ProductDetail;
