import React, { useEffect, useState } from "react";
import { getProducts, deleteProduct } from "../api/api";
import { useNavigate } from "react-router-dom";
import { Container, Typography, Grid, Card, CardContent, CardActions, Button, CircularProgress, Divider, Fab, Dialog, Box } from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import InfoIcon from "@mui/icons-material/Info";
import DeleteIcon from "@mui/icons-material/Delete";
import SearchIcon from '@mui/icons-material/Search';
import InputAdornment from '@mui/material/InputAdornment';
import TextField from '@mui/material/TextField';

function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [deletingId, setDeletingId] = useState(null);
  const [confirmOpen, setConfirmOpen] = useState(false);
  const [toDelete, setToDelete] = useState(null);
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  const fetchProducts = () => {
    setLoading(true);
    getProducts().then(res => {
      setProducts(res.data.products);
      setLoading(false);
    });
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleDelete = (id) => {
    setConfirmOpen(true);
    setToDelete(id);
  };

  const confirmDelete = () => {
    setDeletingId(toDelete);
    deleteProduct(toDelete)
      .then(() => {
        fetchProducts();
      })
      .finally(() => {
        setDeletingId(null);
        setConfirmOpen(false);
        setToDelete(null);
      });
  };

  const filteredProducts = products.filter(product =>
    product.name.toLowerCase().includes(search.toLowerCase()) ||
    (product.category && product.category.toLowerCase().includes(search.toLowerCase())) ||
    (product.batch_number && product.batch_number.toLowerCase().includes(search.toLowerCase()))
  );

  if (loading) return <CircularProgress style={{ margin: 32 }} />;

  return (
    <Container maxWidth="md" style={{ marginTop: 32 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1 }}>
        Products
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
            No products found. Try adding a new product or adjusting your search.
          </Typography>
        </Box>
      ) : (
        <Grid container spacing={3} sx={{ animation: 'fadeInUp 1s' }}>
          {filteredProducts.map((product, idx) => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Card elevation={6} sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                background: 'rgba(255,255,255,0.85)',
                borderRadius: 4,
                boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.12)',
                backdropFilter: 'blur(8px)',
                transition: 'transform 0.25s, box-shadow 0.25s',
                animation: `popIn 0.7s ${0.1 * idx}s`,
                '&:hover': {
                  transform: 'scale(1.045) translateY(-4px)',
                  boxShadow: '0 16px 48px 0 #1976d244',
                },
              }}>
                <CardContent sx={{ flexGrow: 1 }}>
                  <Typography variant="h6" gutterBottom noWrap sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif' }}>{product.name}</Typography>
                  <Typography variant="body2" color="text.secondary">Batch: {product.batch_number}</Typography>
                  <Typography variant="body2" color="text.secondary">Category: {product.category}</Typography>
                  <Typography variant="body2" color="text.secondary">Status: {product.workflow_status}</Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" color="primary" startIcon={<InfoIcon />} onClick={() => navigate(`/products/${product.id}`)} sx={{ fontWeight: 600 }}>
                    Details
                  </Button>
                  <Button size="small" color="error" startIcon={<DeleteIcon />} onClick={() => handleDelete(product.id)} disabled={deletingId === product.id} sx={{ fontWeight: 600 }}>
                    {deletingId === product.id ? <CircularProgress size={18} color="inherit" /> : "Delete"}
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
      <Fab color="secondary" aria-label="add" sx={{
        position: 'fixed',
        bottom: 32,
        right: 32,
        boxShadow: '0 4px 24px 0 #ff980088',
        animation: 'popIn 1.2s',
        fontWeight: 700,
        fontFamily: 'Inter, Roboto, Arial, sans-serif',
        '&:hover': {
          boxShadow: '0 8px 32px 0 #ff9800cc, 0 0 0 8px #fff3e088',
          background: 'linear-gradient(90deg, #ff9800 0%, #ff80ab 100%)',
        },
      }} onClick={() => navigate("/products/new") }>
        <AddIcon />
      </Fab>
      {/* Confirm Delete Dialog */}
      <Dialog open={confirmOpen} onClose={() => setConfirmOpen(false)}>
        <CardContent>
          <Typography>Are you sure you want to delete this product?</Typography>
        </CardContent>
        <CardActions>
          <Button onClick={() => setConfirmOpen(false)}>Cancel</Button>
          <Button color="error" onClick={confirmDelete} disabled={!!deletingId}>
            {deletingId ? <CircularProgress size={18} color="inherit" /> : "Delete"}
          </Button>
        </CardActions>
      </Dialog>
    </Container>
  );
}

export default ProductList;
