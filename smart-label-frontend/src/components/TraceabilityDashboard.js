import React, { useState } from "react";
import { getTraceability } from "../api/api";
import { Container, Typography, TextField, Button, Paper, List, ListItem, ListItemText, Divider, Card, CardContent, Grid, Stack } from "@mui/material";
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
    <Container maxWidth="md" style={{ marginTop: 32 }}>
      <Typography variant="h4" gutterBottom>Traceability Dashboard</Typography>
      <Paper style={{ padding: 16, marginBottom: 24 }}>
        <Stack direction="row" spacing={2} alignItems="center">
          <TextField
            label="Product ID, Batch Number, or Label Data"
            value={identifier}
            onChange={e => setIdentifier(e.target.value)}
            fullWidth
            style={{ marginBottom: 16 }}
          />
          <Button variant="contained" color="primary" onClick={handleSearch} disabled={loading || !identifier} startIcon={<SearchIcon />}>
            {loading ? "Searching..." : "Search"}
          </Button>
        </Stack>
        {error && <Typography color="error" style={{ marginTop: 16 }}>{error}</Typography>}
      </Paper>
      {result && result.success && (
        <Grid container spacing={3}>
          <Grid item xs={12}>
            <Card elevation={3} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.02)', boxShadow: 6 }, mb: 3 }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <InfoIcon color="primary" />
                  <Typography variant="h6">Product Info</Typography>
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
            <Card elevation={2} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.02)', boxShadow: 4 }, mb: 3 }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <FactCheckIcon color="secondary" />
                  <Typography variant="h6">Quality Checks</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.quality_checks.map((qc, idx) => (
                    <ListItem key={idx}>
                      <ListItemText
                        primary={`${qc.parameter_name} (${qc.status})`}
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
            <Card elevation={2} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.02)', boxShadow: 4 }, mb: 3 }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <LabelIcon color="info" />
                  <Typography variant="h6">Labels</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.labels.map((label, idx) => (
                    <ListItem key={idx}>
                      <ListItemText
                        primary={`${label.label_type} (${label.auto_generated ? "Auto" : "Manual"})`}
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
            <Card elevation={2} sx={{ transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.02)', boxShadow: 4 }, mb: 3 }}>
              <CardContent>
                <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                  <HistoryIcon color="warning" />
                  <Typography variant="h6">Workflow Logs</Typography>
                </Stack>
                <Divider />
                <List>
                  {result.workflow_logs.map((log, idx) => (
                    <ListItem key={idx}>
                      <ListItemText
                        primary={`${log.action} (${log.status})`}
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