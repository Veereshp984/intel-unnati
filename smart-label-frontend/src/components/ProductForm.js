import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { createProduct, getIndianProductQualityParameters } from "../api/api";
import { Container, TextField, Button, Typography, Paper, CircularProgress } from "@mui/material";
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
    <Container maxWidth="sm" style={{ marginTop: 32 }}>
      <Paper style={{ padding: 24 }}>
        <Typography variant="h5" gutterBottom>Add New Product</Typography>
        <form onSubmit={handleSubmit}>
          <TextField label="Name" name="name" value={form.name} onChange={handleChange} fullWidth margin="normal" required />
          <TextField label="Description" name="description" value={form.description} onChange={handleChange} fullWidth margin="normal" />
          <TextField label="Category" name="category" value={form.category} onChange={handleChange} fullWidth margin="normal" />
          <TextField label="Manufacturer" name="manufacturer" value={form.manufacturer} onChange={handleChange} fullWidth margin="normal" />
          <TextField label="Batch Number" name="batch_number" value={form.batch_number} onChange={handleChange} fullWidth margin="normal" />
          <TextField label="Manufacturing Date" name="manufacturing_date" type="date" value={form.manufacturing_date} onChange={handleChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
          <TextField label="Expiry Date" name="expiry_date" type="date" value={form.expiry_date} onChange={handleChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
          {error && <Typography color="error" style={{ marginTop: 8 }}>{error}</Typography>}
          <Button type="submit" variant="contained" color="primary" fullWidth style={{ marginTop: 16 }} disabled={loading}>
            {loading ? <CircularProgress size={24} color="inherit" /> : "Create Product"}
          </Button>
        </form>
        {/* Show Indian product quality parameters if found */}
        <div style={{ marginTop: 24 }}>
          {paramsLoading && <CircularProgress size={20} style={{ marginRight: 8 }} />}
          {qualityParams.length > 0 && (
            <>
              <Typography variant="subtitle1" style={{ marginTop: 16 }}>Indian Product Quality Parameters:</Typography>
              <ul style={{ marginTop: 8 }}>
                {qualityParams.map((param, idx) => (
                  <li key={idx}>
                    <b>{param.parameter}</b>: Expected {param.expected} {param.unit} (Tolerance: ±{param.tolerance}{param.unit})
                  </li>
                ))}
              </ul>
            </>
          )}
          {paramsMsg && <Typography color="textSecondary" style={{ marginTop: 8 }}>{paramsMsg}</Typography>}
        </div>
      </Paper>
    </Container>
  );
}

export default ProductForm;
