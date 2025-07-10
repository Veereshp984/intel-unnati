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
      main: '#1976d2',
    },
    secondary: {
      main: '#ff9800',
    },
    background: {
      default: '#f4f6f8',
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
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
    <AppBar position="static" color="primary" sx={{ mb: 3 }}>
      <Toolbar>
        <Box sx={{ display: 'flex', alignItems: 'center', flexGrow: 1 }}>
          <img src="/logo192.png" alt="Logo" style={{ height: 40, marginRight: 16 }} />
          <Typography variant="h6" color="inherit" sx={{ fontWeight: 700, letterSpacing: 1, mr: 4 }}>
            Smart Product Labeling
          </Typography>
          {navLinks.map(link => (
            <Button
              key={link.to}
              component={Link}
              to={link.to}
              color={location.pathname === link.to ? "secondary" : "inherit"}
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
