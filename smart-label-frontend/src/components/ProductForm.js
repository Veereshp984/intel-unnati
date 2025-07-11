import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createProduct, getIndianProductQualityParameters } from "../api/api";
import { Container, TextField, Button, Typography, Paper, CircularProgress, Box } from "@mui/material";
import { useSnackbar } from "./SnackbarProvider";

function ProductForm() {
  const [form, setForm] = useState({
    name: "",
    description: "",
    category: "",
    manufacturer: "",
    batch_number: "",
    manufacturing_date: "",
    expiry_date: ""
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [qualityParams, setQualityParams] = useState([]);
  const [paramsLoading, setParamsLoading] = useState(false);
  const [paramsMsg, setParamsMsg] = useState("");
  const navigate = useNavigate();
  const showSnackbar = useSnackbar();

  // Helper to convert product name to key
  const toProductKey = name => name.toLowerCase().replace(/ /g, "_");

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
    if (e.target.name === "name") {
      const key = toProductKey(e.target.value);
      if (key.length > 2) {
        setParamsLoading(true);
        setParamsMsg("");
        getIndianProductQualityParameters(key)
          .then(res => {
            if (res.data.quality_parameters && res.data.quality_parameters.length > 0) {
              setQualityParams(res.data.quality_parameters);
              setParamsMsg("");
            } else {
              setQualityParams([]);
              setParamsMsg("No Indian quality parameters found for this product name.");
            }
          })
          .catch(() => {
            setQualityParams([]);
            setParamsMsg("No Indian quality parameters found for this product name.");
          })
          .finally(() => setParamsLoading(false));
      } else {
        setQualityParams([]);
        setParamsMsg("");
      }
    }
  };

  const handleSubmit = e => {
    e.preventDefault();
    setLoading(true);
    setError("");
    createProduct(form)
      .then(res => {
        showSnackbar("Product created successfully!", "success");
        navigate("/");
      })
      .catch(err => {
        setError(err.response?.data?.error || "Error creating product");
        showSnackbar(err.response?.data?.error || "Error creating product", "error");
      })
      .finally(() => setLoading(false));
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 6, mb: 6 }}>
      <Paper sx={{
        p: 4,
        borderRadius: 5,
        background: 'rgba(255,255,255,0.85)',
        boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)',
        backdropFilter: 'blur(10px)',
        animation: 'fadeInDown 1s',
      }}>
        <Typography variant="h5" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mb: 2 }}>Add New Product</Typography>
        <form onSubmit={handleSubmit}>
          <TextField label="Name" name="name" value={form.name} onChange={handleChange} fullWidth margin="normal" required sx={{ fontWeight: 600 }} />
          <TextField label="Description" name="description" value={form.description} onChange={handleChange} fullWidth margin="normal" sx={{ fontWeight: 600 }} />
          <TextField label="Category" name="category" value={form.category} onChange={handleChange} fullWidth margin="normal" sx={{ fontWeight: 600 }} />
          <TextField label="Manufacturer" name="manufacturer" value={form.manufacturer} onChange={handleChange} fullWidth margin="normal" sx={{ fontWeight: 600 }} />
          <TextField label="Batch Number" name="batch_number" value={form.batch_number} onChange={handleChange} fullWidth margin="normal" sx={{ fontWeight: 600 }} />
          <TextField label="Manufacturing Date" name="manufacturing_date" type="date" value={form.manufacturing_date} onChange={handleChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} sx={{ fontWeight: 600 }} />
          <TextField label="Expiry Date" name="expiry_date" type="date" value={form.expiry_date} onChange={handleChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} sx={{ fontWeight: 600 }} />
          {error && <Typography color="error" sx={{ mt: 1, fontWeight: 600, animation: 'fadeIn 0.7s' }}>{error}</Typography>}
          <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 3, fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #1976d244', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #1976d244' } }} disabled={loading}>
            {loading ? <CircularProgress size={24} color="inherit" /> : "Create Product"}
          </Button>
        </form>
        {/* Show Indian product quality parameters if found */}
        <Box sx={{ mt: 4 }}>
          {paramsLoading && <CircularProgress size={20} sx={{ mr: 1 }} />}
          {qualityParams.length > 0 && (
            <>
              <Typography variant="subtitle1" sx={{ mt: 2, fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif', animation: 'fadeInUp 0.8s' }}>Indian Product Quality Parameters:</Typography>
              <ul style={{ marginTop: 8 }}>
                {qualityParams.map((param, idx) => (
                  <li key={idx} style={{ fontWeight: 600, animation: `fadeIn 0.7s ${0.1 * idx}s` }}>
                    <b>{param.parameter}</b>: Expected {param.expected} {param.unit} (Tolerance:  b1{param.tolerance}{param.unit})
                  </li>
                ))}
              </ul>
            </>
          )}
          {paramsMsg && <Typography color="textSecondary" sx={{ mt: 2, fontWeight: 500, animation: 'fadeIn 0.7s' }}>{paramsMsg}</Typography>}
        </Box>
      </Paper>
    </Container>
  );
}

export default ProductForm;
