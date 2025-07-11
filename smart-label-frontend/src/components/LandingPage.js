import React from "react";
import { Typography, Button, Stack, Box, Grid, Divider } from "@mui/material";
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
    <Box sx={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #e3f2fd 0%, #ede9fe 100%)',
      py: { xs: 4, md: 8 },
      position: 'relative',
      overflow: 'hidden',
    }}>
      {/* Gradient overlay for hero effect */}
      <Box sx={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: 400,
        background: 'linear-gradient(120deg, #1976d2 0%, #7c3aed 100%)',
        opacity: 0.13,
        zIndex: 0,
        filter: 'blur(16px)',
      }} />
      {/* Hero Card using Box */}
      <Box sx={{
        width: '100%',
        px: { xs: 2, sm: 4, md: 6 },
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        mb: { xs: 4, md: 8 },
      }}>
        <Box sx={{
          width: '100%',
          background: 'rgba(255,255,255,0.80)',
          borderRadius: 6,
          backdropFilter: 'blur(16px)',
          boxShadow: '0 8px 32px 0 rgba(124, 58, 237, 0.13)',
          p: { xs: 2, sm: 4, md: 6 },
          animation: 'fadeInDown 1s',
        }}>
          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
            <QrCodeIcon sx={{ fontSize: 72, color: 'primary.main', filter: 'drop-shadow(0 4px 16px #1976d244)', animation: 'popIn 1.2s' }} />
          </Box>
          <Typography variant="h3" fontWeight={800} fontFamily="Inter, Roboto, Arial, sans-serif" gutterBottom sx={{ letterSpacing: 1 }}>
            Smart Product Labeling & Traceability
          </Typography>
          <Typography variant="h6" color="text.secondary" gutterBottom sx={{ fontWeight: 500 }}>
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
              sx={{
                fontWeight: 700,
                px: 4,
                boxShadow: '0 4px 16px 0 #1976d244',
                transition: 'all 0.2s',
                '&:hover': {
                  background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)',
                  transform: 'translateY(-2px) scale(1.04)',
                  boxShadow: '0 8px 32px 0 #1976d244',
                },
              }}
            >
              View Products
            </Button>
            <Button
              variant="outlined"
              color="secondary"
              size="large"
              startIcon={<AddCircleIcon />}
              onClick={() => navigate("/products/new")}
              sx={{
                fontWeight: 700,
                px: 4,
                borderWidth: 2,
                borderColor: 'secondary.main',
                transition: 'all 0.2s',
                '&:hover': {
                  background: 'linear-gradient(90deg, #ff80ab 0%, #ff9800 100%)',
                  color: '#fff',
                  borderColor: 'secondary.main',
                  transform: 'translateY(-2px) scale(1.04)',
                  boxShadow: '0 8px 32px 0 #ff80ab44',
                },
              }}
            >
              Add Product
            </Button>
            <Button
              variant="outlined"
              color="success"
              size="large"
              startIcon={<CameraAltIcon />}
              onClick={() => navigate("/scan")}
              sx={{
                fontWeight: 700,
                px: 4,
                borderWidth: 2,
                borderColor: 'success.main',
                transition: 'all 0.2s',
                '&:hover': {
                  background: 'linear-gradient(90deg, #43e97b 0%, #38f9d7 100%)',
                  color: '#fff',
                  borderColor: 'success.main',
                  transform: 'translateY(-2px) scale(1.04)',
                  boxShadow: '0 8px 32px 0 #43e97b44',
                },
              }}
            >
              Scan Product Label
            </Button>
          </Stack>
        </Box>
      </Box>

      {/* How it Works Section */}
      <Box sx={{ mt: 8, mb: 6, animation: 'fadeInUp 1.2s', px: { xs: 1, sm: 2, md: 4 } }}>
        <Typography variant="h4" align="center" fontWeight={800} fontFamily="Inter, Roboto, Arial, sans-serif" gutterBottom>How it Works</Typography>
        <Divider sx={{ mb: 4, mx: 'auto', width: 120 }} />
        <Grid container spacing={4} justifyContent="center">
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <AddCircleIcon color="secondary" sx={{ fontSize: 48, mb: 1, filter: 'drop-shadow(0 2px 8px #ff80ab44)', animation: 'popIn 1.2s' }} />
              <Typography variant="subtitle1" fontWeight={700}>Add Product</Typography>
              <Typography variant="body2" color="text.secondary">Enter product details and quality parameters.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <CheckCircleIcon color="success" sx={{ fontSize: 48, mb: 1, filter: 'drop-shadow(0 2px 8px #43e97b44)', animation: 'popIn 1.2s' }} />
              <Typography variant="subtitle1" fontWeight={700}>Quality Check</Typography>
              <Typography variant="body2" color="text.secondary">Run automated quality checks for compliance.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <QrCodeIcon color="primary" sx={{ fontSize: 48, mb: 1, filter: 'drop-shadow(0 2px 8px #1976d244)', animation: 'popIn 1.2s' }} />
              <Typography variant="subtitle1" fontWeight={700}>Generate QR Code</Typography>
              <Typography variant="body2" color="text.secondary">Create and print a smart label for each product.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <TrackChangesIcon color="info" sx={{ fontSize: 48, mb: 1, filter: 'drop-shadow(0 2px 8px #21a1ff44)', animation: 'popIn 1.2s' }} />
              <Typography variant="subtitle1" fontWeight={700}>Trace & Scan</Typography>
              <Typography variant="body2" color="text.secondary">Scan labels to view product history and verify authenticity.</Typography>
            </Stack>
          </Grid>
        </Grid>
      </Box>

      {/* Features Section */}
      <Box sx={{ mt: 8, mb: 6, animation: 'fadeInUp 1.4s', px: { xs: 1, sm: 2, md: 4 } }}>
        <Typography variant="h4" align="center" fontWeight={800} fontFamily="Inter, Roboto, Arial, sans-serif" gutterBottom>Features</Typography>
        <Divider sx={{ mb: 4, mx: 'auto', width: 120 }} />
        <Grid container spacing={4} justifyContent="center">
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <CheckCircleIcon color="success" sx={{ fontSize: 40, filter: 'drop-shadow(0 2px 8px #43e97b44)', animation: 'popIn 1.2s' }} />
              <Typography fontWeight={700}>Automated Quality Checks</Typography>
              <Typography variant="body2" color="text.secondary">Ensure every product meets Indian and global standards.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <QrCodeIcon color="primary" sx={{ fontSize: 40, filter: 'drop-shadow(0 2px 8px #1976d244)', animation: 'popIn 1.2s' }} />
              <Typography fontWeight={700}>Smart QR Labels</Typography>
              <Typography variant="body2" color="text.secondary">Generate, print, and scan QR codes for instant traceability.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <PrintIcon color="secondary" sx={{ fontSize: 40, filter: 'drop-shadow(0 2px 8px #ff80ab44)', animation: 'popIn 1.2s' }} />
              <Typography fontWeight={700}>Easy Printing</Typography>
              <Typography variant="body2" color="text.secondary">Download or print labels in PDF format for packaging.</Typography>
            </Stack>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Stack alignItems="center" spacing={1}>
              <SecurityIcon color="info" sx={{ fontSize: 40, filter: 'drop-shadow(0 2px 8px #21a1ff44)', animation: 'popIn 1.2s' }} />
              <Typography fontWeight={700}>Secure & Transparent</Typography>
              <Typography variant="body2" color="text.secondary">Full traceability and anti-counterfeit protection.</Typography>
            </Stack>
          </Grid>
        </Grid>
      </Box>

      {/* Footer */}
      <Box sx={{ mt: 10, textAlign: 'center', color: 'text.secondary', fontSize: 15, animation: 'fadeIn 2s' }}>
        <Divider sx={{ mb: 2, mx: 'auto', width: 120 }} />
        <Typography variant="body2">
          &copy; {new Date().getFullYear()} Smart Product Labeling & Traceability System. All rights reserved.<br />
          Contact: support@smartlabeling.com
        </Typography>
      </Box>
    </Box>
  );
}

export default LandingPage; 