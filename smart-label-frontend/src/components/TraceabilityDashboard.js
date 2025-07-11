import React, { useState } from "react";
import { getTraceability } from "../api/api";
import { Container, Typography, TextField, Button, Paper, List, ListItem, ListItemText, Divider, Card, CardContent, Grid, Stack, Box } from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';
import InfoIcon from '@mui/icons-material/Info';
import FactCheckIcon from '@mui/icons-material/FactCheck';
import LabelIcon from '@mui/icons-material/Label';
import HistoryIcon from '@mui/icons-material/History';

function TraceabilityDashboard() {
  const [identifier, setIdentifier] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    setLoading(true);
    setError("");
    setResult(null);
    getTraceability(identifier)
      .then(res => {
        setResult(res.data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.response?.data?.error || "Not found");
        setLoading(false);
      });
  };

  return (
    <Container maxWidth="md" sx={{ mt: 6, mb: 6 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mb: 3, animation: 'fadeInDown 0.8s' }}>
        Traceability Dashboard
      </Typography>
      <Paper sx={{
        p: 3,
        mb: 4,
        borderRadius: 4,
        background: 'rgba(255,255,255,0.85)',
        boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)',
        backdropFilter: 'blur(8px)',
        animation: 'fadeInDown 1s',
      }}>
        <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2} alignItems="center">
          <TextField
            label="Product ID, Batch Number, or Label Data"
            value={identifier}
            onChange={e => setIdentifier(e.target.value)}
            fullWidth
            sx={{ fontWeight: 600 }}
          />
          <Button variant="contained" color="primary" onClick={handleSearch} disabled={loading || !identifier} startIcon={<SearchIcon />} sx={{ fontWeight: 700, borderRadius: 2, boxShadow: '0 4px 16px 0 #1976d244', transition: 'all 0.2s', '&:hover': { background: 'linear-gradient(90deg, #1976d2 0%, #21a1ff 100%)', transform: 'translateY(-2px) scale(1.04)', boxShadow: '0 8px 32px 0 #1976d244' } }}>
            {loading ? "Searching..." : "Search"}
          </Button>
        </Stack>
        {error && <Typography color="error" sx={{ mt: 2, fontWeight: 600, animation: 'fadeIn 0.7s' }}>{error}</Typography>}
      </Paper>
      {result && result.success && (
        <Grid container spacing={3} sx={{ animation: 'fadeInUp 1s' }}>
          <Grid item xs={12}>
            <Card elevation={8} sx={{ transition: 'transform 0.25s, box-shadow 0.25s', borderRadius: 4, background: 'rgba(255,255,255,0.90)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', mb: 3, '&:hover': { transform: 'scale(1.02) translateY(-2px)', boxShadow: '0 12px 36px 0 #1976d244' } }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <InfoIcon sx={{ color: '#1976d2', fontSize: 28, filter: 'drop-shadow(0 2px 8px #1976d244)' }} />
                  <Typography variant="h6" sx={{ fontWeight: 700 }}>Product Info</Typography>
                </Stack>
                <Divider />
                <List>
                  <ListItem><ListItemText primary="Name" secondary={result.product.name} /></ListItem>
                  <ListItem><ListItemText primary="Category" secondary={result.product.category} /></ListItem>
                  <ListItem><ListItemText primary="Batch Number" secondary={result.product.batch_number} /></ListItem>
                  <ListItem><ListItemText primary="Manufacturer" secondary={result.product.manufacturer} /></ListItem>
                  <ListItem><ListItemText primary="Manufacturing Date" secondary={result.product.manufacturing_date} /></ListItem>
                  <ListItem><ListItemText primary="Expiry Date" secondary={result.product.expiry_date} /></ListItem>
                  <ListItem><ListItemText primary="Workflow Status" secondary={result.product.workflow_status} /></ListItem>
                  <ListItem><ListItemText primary="Traceability Score" secondary={result.traceability_score} /></ListItem>
                  <ListItem><ListItemText primary="Compliance Status" secondary={result.compliance_status} /></ListItem>
                </List>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <Card elevation={8} sx={{ transition: 'transform 0.25s, box-shadow 0.25s', borderRadius: 4, background: 'rgba(255,255,255,0.90)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', mb: 3, animation: 'fadeInUp 1.1s', '&:hover': { transform: 'scale(1.02) translateY(-2px)', boxShadow: '0 12px 36px 0 #43e97b44' } }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <FactCheckIcon sx={{ color: '#43e97b', fontSize: 26, filter: 'drop-shadow(0 2px 8px #43e97b44)' }} />
                  <Typography variant="h6" sx={{ fontWeight: 700 }}>Quality Checks</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.quality_checks.map((qc, idx) => (
                    <ListItem key={idx} sx={{ animation: `fadeIn 0.7s ${0.1 * idx}s` }}>
                      <ListItemText
                        primary={<span style={{ fontWeight: 600 }}>{`${qc.parameter_name} (${qc.status})`}</span>}
                        secondary={`Expected: ${qc.expected_value}, Actual: ${qc.actual_value}, Unit: ${qc.unit}, Checked by: ${qc.checked_by}`}
                      />
                    </ListItem>
                  ))}
                  {result.quality_checks.length === 0 && <ListItem><ListItemText primary="No quality checks." /></ListItem>}
                </List>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <Card elevation={8} sx={{ transition: 'transform 0.25s, box-shadow 0.25s', borderRadius: 4, background: 'rgba(255,255,255,0.90)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', mb: 3, animation: 'fadeInUp 1.2s', '&:hover': { transform: 'scale(1.02) translateY(-2px)', boxShadow: '0 12px 36px 0 #1976d244' } }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <LabelIcon sx={{ color: '#1976d2', fontSize: 26, filter: 'drop-shadow(0 2px 8px #1976d244)' }} />
                  <Typography variant="h6" sx={{ fontWeight: 700 }}>Labels</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.labels.map((label, idx) => (
                    <ListItem key={idx} sx={{ animation: `fadeIn 0.7s ${0.1 * idx}s` }}>
                      <ListItemText
                        primary={<span style={{ fontWeight: 600 }}>{`${label.label_type} (${label.auto_generated ? "Auto" : "Manual"})`}</span>}
                        secondary={`Data: ${label.label_data}, Print Status: ${label.print_status}, Verified: ${label.is_verified ? "Yes" : "No"}`}
                      />
                    </ListItem>
                  ))}
                  {result.labels.length === 0 && <ListItem><ListItemText primary="No labels." /></ListItem>}
                </List>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12}>
            <Card elevation={8} sx={{ transition: 'transform 0.25s, box-shadow 0.25s', borderRadius: 4, background: 'rgba(255,255,255,0.90)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', mb: 3, animation: 'fadeInUp 1.3s', '&:hover': { transform: 'scale(1.02) translateY(-2px)', boxShadow: '0 12px 36px 0 #ff980044' } }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <HistoryIcon sx={{ color: '#ff9800', fontSize: 26, filter: 'drop-shadow(0 2px 8px #ff980044)' }} />
                  <Typography variant="h6" sx={{ fontWeight: 700 }}>Workflow Logs</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.workflow_logs.map((log, idx) => (
                    <ListItem key={idx} sx={{ animation: `fadeIn 0.7s ${0.1 * idx}s` }}>
                      <ListItemText
                        primary={<span style={{ fontWeight: 600 }}>{`${log.action} (${log.status})`}</span>}
                        secondary={log.details}
                      />
                    </ListItem>
                  ))}
                  {result.workflow_logs.length === 0 && <ListItem><ListItemText primary="No workflow logs." /></ListItem>}
                </List>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      )}
    </Container>
  );
}

export default TraceabilityDashboard; 