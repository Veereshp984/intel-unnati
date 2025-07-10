import React, { useState, useEffect } from "react";
import { getProducts, runBatchWorkflow, generateBatchLabels } from "../api/api";
import { Container, Typography, Button, Checkbox, Grid, Card, CardContent, CardActions, ListItemText, Divider, Fab, CircularProgress, Stack } from "@mui/material";
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import LabelIcon from '@mui/icons-material/Label';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import SearchIcon from '@mui/icons-material/Search';
import InputAdornment from '@mui/material/InputAdornment';
import TextField from '@mui/material/TextField';

function BatchOps() {
  const [products, setProducts] = useState([]);
  const [selected, setSelected] = useState([]);
  const [msg, setMsg] = useState("");
  const [loading, setLoading] = useState(false);
  const [labelLoading, setLabelLoading] = useState(false);
  const [search, setSearch] = useState("");

  useEffect(() => {
    getProducts().then(res => setProducts(res.data.products));
  }, []);

  const handleSelect = (id) => {
    setSelected(selected.includes(id) ? selected.filter(x => x !== id) : [...selected, id]);
  };

  const handleBatchWorkflow = () => {
    setLoading(true);
    runBatchWorkflow(selected)
      .then(res => setMsg(res.data.message))
      .catch(err => setMsg(err.response?.data?.error || "Error running batch workflow"))
      .finally(() => setLoading(false));
  };

  const handleBatchLabels = () => {
    setLabelLoading(true);
    generateBatchLabels(selected)
      .then(res => setMsg(res.data.message))
      .catch(err => setMsg(err.response?.data?.error || "Error generating batch labels"))
      .finally(() => setLabelLoading(false));
  };

  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(search.toLowerCase()) ||
    (product.category && product.category.toLowerCase().includes(search.toLowerCase())) ||
    (product.batch_number && product.batch_number.toLowerCase().includes(search.toLowerCase()))
  );

  return (
    <Container maxWidth="md" style={{ marginTop: 32 }}>
      <Typography variant="h4" gutterBottom>Batch Operations</Typography>
      <Divider sx={{ mb: 2 }} />
      <TextField
        placeholder="Search by name, category, or batch..."
        value={search}
        onChange={e => setSearch(e.target.value)}
        fullWidth
        size="small"
        sx={{ mb: 3 }}
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        }}
      />
      {filteredProducts.length === 0 ? (
        <Typography color="text.secondary" align="center" sx={{ mt: 8 }}>
          No products found. Try adjusting your search.
        </Typography>
      ) : (
        <Grid container spacing={3}>
          {filteredProducts.map(product => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Card elevation={3} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 8 } }}>
                <CardContent>
                  <Stack direction="row" alignItems="center" spacing={1} mb={1}>
                    <Checkbox checked={selected.includes(product.id)} onChange={() => handleSelect(product.id)} color="primary" />
                    <Typography variant="h6" noWrap>{product.name}</Typography>
                  </Stack>
                  <Typography variant="body2" color="text.secondary">Batch: {product.batch_number}</Typography>
                  <Typography variant="body2" color="text.secondary">Category: {product.category}</Typography>
                  <Typography variant="body2" color="text.secondary">Status: {product.workflow_status}</Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" color="primary" startIcon={<CheckCircleIcon />} onClick={() => handleSelect(product.id)}>
                    {selected.includes(product.id) ? "Selected" : "Select"}
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
      <Stack direction="row" spacing={2} mt={4}>
        <Button
          variant="contained"
          color="primary"
          startIcon={<PlayArrowIcon />}
          onClick={handleBatchWorkflow}
          disabled={loading || selected.length === 0}
        >
          {loading ? <CircularProgress size={20} color="inherit" /> : "Run Batch Workflow"}
        </Button>
        <Button
          variant="contained"
          color="secondary"
          startIcon={<LabelIcon />}
          onClick={handleBatchLabels}
          disabled={labelLoading || selected.length === 0}
        >
          {labelLoading ? <CircularProgress size={20} color="inherit" /> : "Generate Batch Labels"}
        </Button>
      </Stack>
      {msg && <Typography color="info.main" mt={2}>{msg}</Typography>}
    </Container>
  );
}

export default BatchOps;
