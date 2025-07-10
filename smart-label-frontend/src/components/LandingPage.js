import React from "react";
import { Container, Typography, Button, Stack, Box, Paper, Grid, Divider } from "@mui/material";
import QrCodeIcon from '@mui/icons-material/QrCode';
import InventoryIcon from '@mui/icons-material/Inventory';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import TrackChangesIcon from '@mui/icons-material/TrackChanges';
import PrintIcon from '@mui/icons-material/Print';
import SecurityIcon from '@mui/icons-material/Security';
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();
  return (
    <Box sx={{ minHeight: '100vh', background: 'linear-gradient(135deg, #e3f2fd 0%, #fce4ec 100%)', py: 8 }}>
      <Container maxWidth="md">
        <Paper elevation={4} sx={{ p: { xs: 3, sm: 6 }, textAlign: 'center', borderRadius: 4 }}>
          <QrCodeIcon sx={{ fontSize: 64, color: 'primary.main', mb: 2 }} />
          <Typography variant="h3" fontWeight={700} gutterBottom>
            Smart Product Labeling & Traceability
          </Typography>
          <Typography variant="h6" color="text.secondary" gutterBottom>
            Automate quality checks, generate QR code labels, and ensure product traceability with ease.
          </Typography>
          <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
            This system helps you verify product quality, generate and print smart labels, and track every product from creation to delivery. Scan QR codes to instantly view product details and traceability history.
          </Typography>
          <Stack direction={{ xs: 'column', sm: 'row' }} spacing={3} justifyContent="center" sx={{ mb: 2 }}>
            <Button
              variant="contained"
              color="primary"
              size="large"
              startIcon={<InventoryIcon />}
              onClick={() => navigate("/products")}
            >
              View Products
            </Button>
            <Button
              variant="outlined"
              color="secondary"
              size="large"
              startIcon={<AddCircleIcon />}
              onClick={() => navigate("/products/new")}
            >
              Add Product
            </Button>
            <Button
              variant="outlined"
              color="success"
              size="large"
              startIcon={<CameraAltIcon />}
              onClick={() => navigate("/scan")}
            >
              Scan Product Label
            </Button>
          </Stack>
        </Paper>

        {/* How it Works Section */}
        <Box sx={{ mt: 8, mb: 6 }}>
          <Typography variant="h4" align="center" fontWeight={700} gutterBottom>How it Works</Typography>
          <Divider sx={{ mb: 4, mx: 'auto', width: 120 }} />
          <Grid container spacing={4} justifyContent="center">
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <AddCircleIcon color="secondary" sx={{ fontSize: 40 }} />
                <Typography variant="subtitle1" fontWeight={600}>Add Product</Typography>
                <Typography variant="body2" color="text.secondary">Enter product details and quality parameters.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <CheckCircleIcon color="success" sx={{ fontSize: 40 }} />
                <Typography variant="subtitle1" fontWeight={600}>Quality Check</Typography>
                <Typography variant="body2" color="text.secondary">Run automated quality checks for compliance.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <QrCodeIcon color="primary" sx={{ fontSize: 40 }} />
                <Typography variant="subtitle1" fontWeight={600}>Generate QR Code</Typography>
                <Typography variant="body2" color="text.secondary">Create and print a smart label for each product.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <TrackChangesIcon color="info" sx={{ fontSize: 40 }} />
                <Typography variant="subtitle1" fontWeight={600}>Trace & Scan</Typography>
                <Typography variant="body2" color="text.secondary">Scan labels to view product history and verify authenticity.</Typography>
              </Stack>
            </Grid>
          </Grid>
        </Box>

        {/* Features Section */}
        <Box sx={{ mt: 8, mb: 6 }}>
          <Typography variant="h4" align="center" fontWeight={700} gutterBottom>Features</Typography>
          <Divider sx={{ mb: 4, mx: 'auto', width: 120 }} />
          <Grid container spacing={4} justifyContent="center">
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <CheckCircleIcon color="success" sx={{ fontSize: 32 }} />
                <Typography fontWeight={600}>Automated Quality Checks</Typography>
                <Typography variant="body2" color="text.secondary">Ensure every product meets Indian and global standards.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <QrCodeIcon color="primary" sx={{ fontSize: 32 }} />
                <Typography fontWeight={600}>Smart QR Labels</Typography>
                <Typography variant="body2" color="text.secondary">Generate, print, and scan QR codes for instant traceability.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <PrintIcon color="secondary" sx={{ fontSize: 32 }} />
                <Typography fontWeight={600}>Easy Printing</Typography>
                <Typography variant="body2" color="text.secondary">Download or print labels in PDF format for packaging.</Typography>
              </Stack>
            </Grid>
            <Grid item xs={12} sm={6} md={3}>
              <Stack alignItems="center" spacing={1}>
                <SecurityIcon color="info" sx={{ fontSize: 32 }} />
                <Typography fontWeight={600}>Secure & Transparent</Typography>
                <Typography variant="body2" color="text.secondary">Full traceability and anti-counterfeit protection.</Typography>
              </Stack>
            </Grid>
          </Grid>
        </Box>

        {/* Footer */}
        <Box sx={{ mt: 10, textAlign: 'center', color: 'text.secondary', fontSize: 15 }}>
          <Divider sx={{ mb: 2, mx: 'auto', width: 120 }} />
          <Typography variant="body2">
            &copy; {new Date().getFullYear()} Smart Product Labeling & Traceability System. All rights reserved.<br />
            Contact: support@smartlabeling.com
          </Typography>
        </Box>
      </Container>
    </Box>
  );
}

export default LandingPage; 