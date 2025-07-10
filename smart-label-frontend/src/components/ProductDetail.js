import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getProduct, updateProduct, deleteProduct, runProductWorkflow, clearAutoQualityChecks, clearAutoLabels } from "../api/api";
import { Container, Typography, CircularProgress, Paper, Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle, List, ListItem, ListItemText } from "@mui/material";
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
      <Typography variant="h4" gutterBottom>{product.name}</Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Card elevation={2} sx={{ mb: 2 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Product Information</Typography>
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
          <Card elevation={2} sx={{ mb: 2, p: 2 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Actions</Typography>
              <Divider sx={{ mb: 2 }} />
              <Grid container spacing={1}>
                <Grid item xs={12} sm={6}>
                  <Button
                    variant="outlined"
                    color="warning"
                    fullWidth
                    sx={{ mb: 1 }}
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
                    sx={{ mb: 1 }}
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
                  <Button variant="contained" color="primary" fullWidth sx={{ mb: 1 }} onClick={() => setEditOpen(true)}>
                    Edit
                  </Button>
                </Grid>
                <Grid item xs={12} sm={6}>
                  <Button variant="contained" color="secondary" fullWidth sx={{ mb: 1 }} onClick={handleDelete}>
                    Delete
                  </Button>
                </Grid>
                <Grid item xs={12}>
                  <Button
                    variant="contained"
                    color="primary"
                    fullWidth
                    sx={{ mb: 1 }}
                    onClick={handleRunWorkflow}
                    disabled={workflowLoading}
                  >
                    Run Workflow Automation
                  </Button>
                  {workflowLoading && <CircularProgress size={24} sx={{ ml: 2, verticalAlign: "middle" }} />}
                  {workflowMsg && <Typography color="secondary">{workflowMsg}</Typography>}
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <Card elevation={2} sx={{ mb: 2 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Quality Checks</Typography>
              <Divider sx={{ mb: 2 }} />
              <QualityChecks
                productId={product.id}
                qualityChecks={product.quality_checks || []}
                refresh={() => {
                  getProduct(id).then(res => setProduct(res.data.product));
                }}
              />
            </CardContent>
          </Card>
          <Card elevation={2} sx={{ mb: 2 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Labels</Typography>
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
          <Card elevation={2} sx={{ mb: 2 }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Workflow Logs</Typography>
              <Divider sx={{ mb: 2 }} />
              <List>
                {(product.workflow_logs || []).map((log, idx) => (
                  <ListItem key={idx} sx={{ borderBottom: '1px solid #eee' }}>
                    <ListItemText
                      primary={`${log.action} (${log.status})`}
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
          <DialogContent>
            <TextField label="Name" name="name" value={editForm.name || ""} onChange={handleEditChange} fullWidth required margin="normal" />
            <TextField label="Description" name="description" value={editForm.description || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Category" name="category" value={editForm.category || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Manufacturer" name="manufacturer" value={editForm.manufacturer || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Batch Number" name="batch_number" value={editForm.batch_number || ""} onChange={handleEditChange} fullWidth margin="normal" />
            <TextField label="Manufacturing Date" name="manufacturing_date" type="date" value={editForm.manufacturing_date ? editForm.manufacturing_date.substring(0,10) : ""} onChange={handleEditChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
            <TextField label="Expiry Date" name="expiry_date" type="date" value={editForm.expiry_date ? editForm.expiry_date.substring(0,10) : ""} onChange={handleEditChange} fullWidth margin="normal" InputLabelProps={{ shrink: true }} />
            {error && <Typography color="error">{error}</Typography>}
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setEditOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" color="primary">Save</Button>
          </DialogActions>
        </form>
      </Dialog>
    </Container>
  );
}
export default ProductDetail;
