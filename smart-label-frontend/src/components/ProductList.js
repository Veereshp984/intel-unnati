import React, { useEffect, useState } from "react";
import { getProducts, deleteProduct } from "../api/api";
import { useNavigate } from "react-router-dom";
import { Container, Typography, Grid, Card, CardContent, CardActions, Button, CircularProgress, Divider, Fab, Dialog } from "@mui/material";
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
      <Typography variant="h4" gutterBottom>Products</Typography>
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
          No products found. Try adding a new product or adjusting your search.
        </Typography>
      ) : (
        <Grid container spacing={3}>
          {filteredProducts.map(product => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <Card elevation={3} sx={{ height: '100%', display: 'flex', flexDirection: 'column', transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 8 } }}>
                <CardContent sx={{ flexGrow: 1 }}>
                  <Typography variant="h6" gutterBottom noWrap>{product.name}</Typography>
                  <Typography variant="body2" color="text.secondary">Batch: {product.batch_number}</Typography>
                  <Typography variant="body2" color="text.secondary">Category: {product.category}</Typography>
                  <Typography variant="body2" color="text.secondary">Status: {product.workflow_status}</Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" color="primary" startIcon={<InfoIcon />} onClick={() => navigate(`/products/${product.id}`)}>
                    Details
                  </Button>
                  <Button size="small" color="error" startIcon={<DeleteIcon />} onClick={() => handleDelete(product.id)} disabled={deletingId === product.id}>
                    {deletingId === product.id ? <CircularProgress size={18} color="inherit" /> : "Delete"}
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
      <Fab color="secondary" aria-label="add" style={{ position: 'fixed', bottom: 32, right: 32 }} onClick={() => navigate("/products/new") }>
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
