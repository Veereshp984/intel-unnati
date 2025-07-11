import React, { useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from "react-router-dom";
import ProductList from "./components/ProductList";
import ProductDetail from "./components/ProductDetail";
import ProductForm from "./components/ProductForm";
import BatchOps from "./components/BatchOps";
import TraceabilityDashboard from "./components/TraceabilityDashboard";
import AnalyticsDashboard from "./components/AnalyticsDashboard";
import Scan from "./components/Scan";
import LandingPage from "./components/LandingPage";
import { AppBar, Toolbar, Button, Container, CssBaseline, Box, Typography } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import './App.css';
import { SnackbarProvider } from "./components/SnackbarProvider";

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // blue
    },
    secondary: {
      main: '#7c3aed', // purple
    },
    accent: {
      main: '#21a1ff', // light blue
    },
    background: {
      default: '#f3f4fd', // light blue-purple
    },
  },
  typography: {
    fontFamily: 'Inter, Roboto, Arial, sans-serif',
    fontWeightBold: 700,
  },
  components: {
    MuiAppBar: {
      styleOverrides: {
        root: {
          background: 'rgba(255,255,255,0.7)',
          backdropFilter: 'blur(12px)',
          boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.15)',
          borderBottom: '1px solid #ede9fe',
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: '8px',
          fontWeight: 600,
          transition: 'all 0.2s',
          boxShadow: '0 2px 8px 0 rgba(25, 118, 210, 0.08)',
          '&:hover': {
            background: 'linear-gradient(90deg, #1976d2 0%, #7c3aed 100%)',
            color: '#fff',
            boxShadow: '0 4px 16px 0 rgba(124, 58, 237, 0.16)',
          },
        },
      },
    },
    MuiContainer: {
      styleOverrides: {
        root: {
          background: 'rgba(255,255,255,0.85)',
          borderRadius: '24px',
          boxShadow: '0 8px 32px 0 rgba(124, 58, 237, 0.10)',
          padding: '32px 24px',
          marginTop: '32px',
        },
      },
    },
  },
});

const navLinks = [
  { to: "/", label: "Home" },
  { to: "/batch", label: "Batch Ops" },
  { to: "/trace", label: "Traceability Dashboard" },
  { to: "/analytics", label: "Analytics Dashboard" },
  { to: "/scan", label: "Scan" },
];

function NavBar() {
  const location = useLocation();
  return (
    <AppBar position="static" color="primary" sx={{ mb: 3, borderRadius: 3, mt: 2, mx: 'auto', maxWidth: 1200 }}>
      <Toolbar>
        <Box sx={{ display: 'flex', alignItems: 'center', flexGrow: 1 }}>
          <img src="/logo192.png" alt="Logo" style={{ height: 40, marginRight: 16, borderRadius: 8, boxShadow: '0 2px 8px rgba(25,118,210,0.10)' }} />
          <Typography variant="h5" color="primary" sx={{ fontWeight: 700, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mr: 4, textShadow: '0 2px 8px rgba(25,118,210,0.10)' }}>
            Smart Product Labeling
          </Typography>
          {navLinks.map(link => (
            <Button
              key={link.to}
              component={Link}
              to={link.to}
              color={location.pathname === link.to ? "secondary" : "primary"}
              variant={location.pathname === link.to ? "contained" : "text"}
              sx={{ mr: 2 }}
            >
              {link.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
}

function App() {
  useEffect(() => {
    document.body.style.background = "linear-gradient(135deg, #e3f2fd 0%, #f4f6fa 100%)";
  }, []);
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <SnackbarProvider>
        <Router>
          <NavBar />
          <Container maxWidth="lg" sx={{ mt: 4 }}>
            <Routes>
              <Route path="/" element={<LandingPage />} />
              <Route path="/products" element={<ProductList />} />
              <Route path="/products/new" element={<ProductForm />} />
              <Route path="/products/:id" element={<ProductDetail />} />
              <Route path="/batch" element={<BatchOps />} />
              <Route path="/trace" element={<TraceabilityDashboard />} />
              <Route path="/analytics" element={<AnalyticsDashboard />} />
              <Route path="/scan" element={<Scan />} />
              {/* More routes in future phases */}
            </Routes>
          </Container>
        </Router>
      </SnackbarProvider>
    </ThemeProvider>
  );
}

export default App;
