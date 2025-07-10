import React, { useEffect, useState } from "react";
import { getAnalyticsDashboard, getQualityTrends, getCategoryBreakdown } from "../api/api";
import { Container, Typography, Paper, Grid, CircularProgress, Card, CardContent, Divider, Stack } from "@mui/material";
import AssessmentIcon from '@mui/icons-material/Assessment';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import PieChartIcon from '@mui/icons-material/PieChart';
import PercentIcon from '@mui/icons-material/Percent';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from "recharts";

const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#8884d8", "#82ca9d"];

function AnalyticsDashboard() {
  const [dashboard, setDashboard] = useState(null);
  const [trends, setTrends] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      getAnalyticsDashboard(),
      getQualityTrends(),
      getCategoryBreakdown()
    ]).then(([dashRes, trendRes, catRes]) => {
      setDashboard(dashRes.data);
      setTrends(trendRes.data.trends || []);
      setCategories(catRes.data.category_breakdown || []);
      setLoading(false);
    });
  }, []);

  if (loading) return <CircularProgress style={{ margin: 32 }} />;

  return (
    <Container maxWidth="lg" style={{ marginTop: 32 }}>
      <Typography variant="h4" gutterBottom>Analytics Dashboard</Typography>
      <Grid container spacing={3}>
        {/* Summary Cards */}
        <Grid item xs={12} md={4}>
          <Card elevation={3} sx={{ height: '100%', transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 8 } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <AssessmentIcon color="primary" />
                <Typography variant="h6">Summary</Typography>
              </Stack>
              <Divider />
              <Typography>Total Products: {dashboard.total_products}</Typography>
              <Typography>Total Quality Checks: {dashboard.total_quality_checks}</Typography>
              <Typography>Passed Checks: {dashboard.passed_checks}</Typography>
              <Typography>Failed Checks: {dashboard.failed_checks}</Typography>
              <Typography>Total Labels: {dashboard.total_labels}</Typography>
              <Typography>Verified Labels: {dashboard.verified_labels}</Typography>
              <Typography>Completed Workflows: {dashboard.completed_workflows}</Typography>
              <Typography>Failed Workflows: {dashboard.failed_workflows}</Typography>
              <Typography>In Progress Workflows: {dashboard.in_progress_workflows}</Typography>
            </CardContent>
          </Card>
        </Grid>
        {/* Quality Trends Chart */}
        <Grid item xs={12} md={8}>
          <Card elevation={3} sx={{ height: '100%', transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 8 } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <TrendingUpIcon color="secondary" />
                <Typography variant="h6">Quality Trends (Last 30 Days)</Typography>
              </Stack>
              <Divider />
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={trends} margin={{ top: 5, right: 20, left: 0, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="date" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="passed" stroke="#4caf50" name="Passed" />
                  <Line type="monotone" dataKey="failed" stroke="#f44336" name="Failed" />
                  <Line type="monotone" dataKey="total" stroke="#2196f3" name="Total" />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
        {/* Category Breakdown Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={2} sx={{ height: '100%', transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 6 } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <PieChartIcon color="info" />
                <Typography variant="h6">Category Breakdown</Typography>
              </Stack>
              <Divider />
              <ResponsiveContainer width="100%" height={250}>
                <PieChart>
                  <Pie
                    data={categories}
                    dataKey="count"
                    nameKey="category"
                    cx="50%"
                    cy="50%"
                    outerRadius={80}
                    fill="#8884d8"
                    label
                  >
                    {categories.map((entry, idx) => (
                      <Cell key={`cell-${idx}`} fill={COLORS[idx % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                  <Legend />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
        {/* Rates */}
        <Grid item xs={12} md={6}>
          <Card elevation={2} sx={{ height: '100%', transition: 'transform 0.2s, box-shadow 0.2s', '&:hover': { transform: 'scale(1.03)', boxShadow: 6 } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <PercentIcon color="success" />
                <Typography variant="h6">Rates</Typography>
              </Stack>
              <Divider />
              <Typography>Quality Pass Rate: {dashboard.quality_pass_rate.toFixed(1)}%</Typography>
              <Typography>Label Verification Rate: {dashboard.label_verification_rate.toFixed(1)}%</Typography>
              <Typography>Workflow Completion Rate: {dashboard.workflow_completion_rate.toFixed(1)}%</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default AnalyticsDashboard; 