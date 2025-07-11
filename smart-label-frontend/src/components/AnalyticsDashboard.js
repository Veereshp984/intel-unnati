import React, { useEffect, useState } from "react";
import { getAnalyticsDashboard, getQualityTrends, getCategoryBreakdown } from "../api/api";
import { Container, Typography, Paper, Grid, CircularProgress, Card, CardContent, Divider, Stack, Box } from "@mui/material";
import AssessmentIcon from '@mui/icons-material/Assessment';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import PieChartIcon from '@mui/icons-material/PieChart';
import PercentIcon from '@mui/icons-material/Percent';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from "recharts";

const COLORS = ["#1976d2", "#00C49F", "#FFBB28", "#FF80AB", "#8884d8", "#82ca9d"];

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
    <Container maxWidth="lg" sx={{ mt: 6, mb: 6 }}>
      <Typography variant="h4" gutterBottom sx={{ fontWeight: 800, fontFamily: 'Inter, Roboto, Arial, sans-serif', letterSpacing: 1, mb: 3, animation: 'fadeInDown 0.8s' }}>
        Analytics Dashboard
      </Typography>
      <Grid container spacing={3}>
        {/* Summary Cards */}
        <Grid item xs={12} md={4}>
          <Card elevation={8} sx={{ height: '100%', borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', transition: 'transform 0.25s, box-shadow 0.25s', animation: 'fadeInUp 1s', '&:hover': { transform: 'scale(1.045) translateY(-4px)', boxShadow: '0 16px 48px 0 #1976d244' } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <AssessmentIcon sx={{ color: '#1976d2', fontSize: 32, filter: 'drop-shadow(0 2px 8px #1976d244)' }} />
                <Typography variant="h6" sx={{ fontWeight: 700 }}>Summary</Typography>
              </Stack>
              <Divider />
              <Typography>Total Products: <b>{dashboard.total_products}</b></Typography>
              <Typography>Total Quality Checks: <b>{dashboard.total_quality_checks}</b></Typography>
              <Typography>Passed Checks: <b style={{ color: '#43e97b' }}>{dashboard.passed_checks}</b></Typography>
              <Typography>Failed Checks: <b style={{ color: '#ff80ab' }}>{dashboard.failed_checks}</b></Typography>
              <Typography>Total Labels: <b>{dashboard.total_labels}</b></Typography>
              <Typography>Verified Labels: <b style={{ color: '#1976d2' }}>{dashboard.verified_labels}</b></Typography>
              <Typography>Completed Workflows: <b style={{ color: '#43e97b' }}>{dashboard.completed_workflows}</b></Typography>
              <Typography>Failed Workflows: <b style={{ color: '#ff80ab' }}>{dashboard.failed_workflows}</b></Typography>
              <Typography>In Progress Workflows: <b style={{ color: '#ff9800' }}>{dashboard.in_progress_workflows}</b></Typography>
            </CardContent>
          </Card>
        </Grid>
        {/* Quality Trends Chart */}
        <Grid item xs={12} md={8}>
          <Card elevation={8} sx={{ height: '100%', borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', transition: 'transform 0.25s, box-shadow 0.25s', animation: 'fadeInUp 1.1s', '&:hover': { transform: 'scale(1.03) translateY(-2px)', boxShadow: '0 12px 36px 0 #1976d244' } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <TrendingUpIcon sx={{ color: '#ff9800', fontSize: 32, filter: 'drop-shadow(0 2px 8px #ff980044)' }} />
                <Typography variant="h6" sx={{ fontWeight: 700 }}>Quality Trends (Last 30 Days)</Typography>
              </Stack>
              <Divider />
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={trends} margin={{ top: 5, right: 20, left: 0, bottom: 5 }}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="date" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Line type="monotone" dataKey="passed" stroke="#43e97b" name="Passed" strokeWidth={3} />
                  <Line type="monotone" dataKey="failed" stroke="#ff80ab" name="Failed" strokeWidth={3} />
                  <Line type="monotone" dataKey="total" stroke="#1976d2" name="Total" strokeWidth={3} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
        {/* Category Breakdown Chart */}
        <Grid item xs={12} md={6}>
          <Card elevation={8} sx={{ height: '100%', borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', transition: 'transform 0.25s, box-shadow 0.25s', animation: 'fadeInUp 1.2s', '&:hover': { transform: 'scale(1.03) translateY(-2px)', boxShadow: '0 12px 36px 0 #1976d244' } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <PieChartIcon sx={{ color: '#1976d2', fontSize: 32, filter: 'drop-shadow(0 2px 8px #1976d244)' }} />
                <Typography variant="h6" sx={{ fontWeight: 700 }}>Category Breakdown</Typography>
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
                    fill="#1976d2"
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
          <Card elevation={8} sx={{ height: '100%', borderRadius: 4, background: 'rgba(255,255,255,0.85)', boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.14)', backdropFilter: 'blur(8px)', transition: 'transform 0.25s, box-shadow 0.25s', animation: 'fadeInUp 1.3s', '&:hover': { transform: 'scale(1.03) translateY(-2px)', boxShadow: '0 12px 36px 0 #1976d244' } }}>
            <CardContent>
              <Stack direction="row" alignItems="center" spacing={1} mb={2}>
                <PercentIcon sx={{ color: '#43e97b', fontSize: 32, filter: 'drop-shadow(0 2px 8px #43e97b44)' }} />
                <Typography variant="h6" sx={{ fontWeight: 700 }}>Rates</Typography>
              </Stack>
              <Divider />
              <Typography>Quality Pass Rate: <b style={{ color: '#43e97b' }}>{dashboard.quality_pass_rate.toFixed(1)}%</b></Typography>
              <Typography>Label Verification Rate: <b style={{ color: '#1976d2' }}>{dashboard.label_verification_rate.toFixed(1)}%</b></Typography>
              <Typography>Workflow Completion Rate: <b style={{ color: '#ff9800' }}>{dashboard.workflow_completion_rate.toFixed(1)}%</b></Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default AnalyticsDashboard; 