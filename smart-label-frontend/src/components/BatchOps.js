import React, { useState, useEffect } from "react";
import { getProducts, runBatchWorkflow, generateBatchLabels } from "../api/api";
import { Container, Typography, Button, Checkbox, Grid, Card, CardContent, CardActions, ListItemText, Divider, Fab, CircularProgress, Stack, Box } from "@mui/material";
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
    <Container maxWidth="md" sx={{ mt: 6, mb: 6 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mb: 3, animation: 'fadeInDown 0.8s' }}>
        Batch Operations
      </Typography>
      <Divider sx={{ mb: 2 }} />
      <Box sx={{
        mb: 3,
        background: 'rgba(255,255,255,0.7)',
        borderRadius: 3,
        boxShadow: '0 4px 16px 0 rgba(31, 38, 135, 0.10)',
        backdropFilter: 'blur(8px)',
        p: 1.5,
        animation: 'fadeInDown 0.8s',
      }}>
        <TextField
          placeholder="Search by name, category, or batch..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          fullWidth
          size="small"
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            ),
            style: { fontWeight: 500, fontFamily: 'Inter, Roboto, Arial, sans-serif' }
          }}
        />
      </Box>
      {filteredProducts.length === 0 ? (
        <Box sx={{ textAlign: 'center', mt: 8, animation: 'fadeIn 1s' }}>
          <img src="https://undraw.co/api/illustrations/empty?color=1976d2" alt="No products" style={{ width: 180, opacity: 0.7, marginBottom: 16 }} />
          <Typography color="text.secondary" sx={{ fontWeight: 500, fontSize: 18 }}>
            No products found. Try adjusting your search.
          </Typography>
        </Box>
      ) : (
        <Grid container spacing={3} sx={{ animation: 'fadeInUp 1s' }}>
          {filteredProducts.map((product, idx) => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Card elevation={8} sx={{
                transition: 'transform 0.25s, box-shadow 0.25s',
                borderRadius: 4,
                background: 'rgba(255,255,255,0.85)',
                boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)',
                backdropFilter: 'blur(8px)',
                animation: `popIn 0.7s ${0.1 * idx}s`,
                '&:hover': {
                  transform: 'scale(1.045) translateY(-4px)',
                  boxShadow: '0 16px 48px 0 #1976d244',
                },
              }}>
                <CardContent>
                  <Stack direction="row" alignItems="center" spacing={1} mb={1}>
                    <Checkbox checked={selected.includes(product.id)} onChange={() => handleSelect(product.id)} color="primary" />
                    <Typography variant="h6" noWrap sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>{product.name}</Typography>
                  </Stack>
                  <Typography variant="body2" color="text.secondary">Batch: {product.batch_number}</Typography>
                  <Typography variant="body2" color="text.secondary">Category: {product.category}</Typography>
                  <Typography variant="body2" color="text.secondary">Status: {product.workflow_status}</Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" color="primary" startIcon={<CheckCircleIcon />} onClick={() => handleSelect(product.id)} sx={{ fontWeight: 600 }}>
                    {selected.includes(product.id) ? "Selected" : "Select"}
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
      <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2} mt={4} sx={{ animation: 'fadeInUp 1.2s' }}>
        <Button
          variant="contained"
          color="primary"
          startIcon={<PlayArrowIcon />}
          onClick={handleBatchWorkflow}
          disabled={loading || selected.length === 0}
          sx={{ fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #1976d244', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #1976d244' } }}
        >
          {loading ? <CircularProgress size={20} color="inherit" /> : "Run Batch Workflow"}
        </Button>
        <Button
          variant="contained"
          color="secondary"
          startIcon={<LabelIcon />}
          onClick={handleBatchLabels}
          disabled={labelLoading || selected.length === 0}
          sx={{ fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #ff80ab44', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #ff80ab 0%, #ff9800 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #ff80ab44' } }}
        >
          {labelLoading ? <CircularProgress size={20} color="inherit" /> : "Generate Batch Labels"}
        </Button>
      </Stack>
      {msg && <Typography color="info.main" mt={2} sx={{ fontWeight: 600, animation: 'fadeIn 1s' }}>{msg}</Typography>}
    </Container>
  );
}

export default BatchOps;
