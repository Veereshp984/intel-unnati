import React, { useState } from "react";
import { createQualityCheck, runAutoQualityChecks } from "../api/api";
import { Typography, List, ListItem, ListItemText, Button, Dialog, DialogTitle, DialogContent, TextField, DialogActions } from "@mui/material";

function QualityChecks({ productId, qualityChecks, refresh }) {
  const [open, setOpen] = useState(false);
  const [form, setForm] = useState({ parameter_name: "", expected_value: "", actual_value: "", unit: "", status: "pending", checked_by: "", notes: "", tolerance: "" });
  const [error, setError] = useState("");

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = e => {
    e.preventDefault();
    if (!form.parameter_name) {
      setError("Parameter name is required");
      return;
    }
    createQualityCheck(productId, form)
      .then(() => {
        setOpen(false);
        setForm({ parameter_name: "", expected_value: "", actual_value: "", unit: "", status: "pending", checked_by: "", notes: "", tolerance: "" });
        refresh();
      })
      .catch(err => setError(err.response?.data?.error || "Error creating quality check"));
  };

  const handleAuto = () => {
    runAutoQualityChecks(productId).then(refresh);
  };

  return (
    <div>
      <Typography variant="h6" gutterBottom>Quality Checks</Typography>
      <Button variant="contained" color="primary" onClick={() => setOpen(true)} style={{ marginRight: 8 }}>
        Add Quality Check
      </Button>
      <Button variant="outlined" color="secondary" onClick={handleAuto}>
        Run Auto Quality Checks
      </Button>
      <List>
        {qualityChecks.map((qc, idx) => (
          <ListItem key={idx}>
            <ListItemText
              primary={`${qc.parameter_name} (${qc.status})`}
              secondary={`Expected: ${qc.expected_value}, Actual: ${qc.actual_value}, Unit: ${qc.unit}, Checked by: ${qc.checked_by}, Notes: ${qc.notes}`}
            />
          </ListItem>
        ))}
      </List>
      <Dialog open={open} onClose={() => setOpen(false)}>
        <DialogTitle>Add Quality Check</DialogTitle>
        <form onSubmit={handleSubmit}>
          <DialogContent>
            <TextField label="Parameter Name" name="parameter_name" value={form.parameter_name} onChange={handleChange} fullWidth required margin="normal" />
            <TextField label="Expected Value" name="expected_value" value={form.expected_value} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Actual Value" name="actual_value" value={form.actual_value} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Unit" name="unit" value={form.unit} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Status" name="status" value={form.status} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Checked By" name="checked_by" value={form.checked_by} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Notes" name="notes" value={form.notes} onChange={handleChange} fullWidth margin="normal" />
            <TextField label="Tolerance" name="tolerance" value={form.tolerance} onChange={handleChange} fullWidth margin="normal" />
            {error && <Typography color="error">{error}</Typography>}
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" color="primary">Add</Button>
          </DialogActions>
        </form>
      </Dialog>
    </div>
  );
}
export default QualityChecks;
