import React, { useRef, useState, useCallback, useEffect } from "react";
import Webcam from "react-webcam";
import jsQR from "jsqr";
import { getTraceability } from "../api/api";
import { Container, Typography, Paper, Button, CircularProgress, Box, Alert, Divider } from "@mui/material";
import CameraAltIcon from '@mui/icons-material/CameraAlt';

const videoConstraints = {
  facingMode: "environment"
};

function Scan() {
  const webcamRef = useRef(null);
  const [scanning, setScanning] = useState(false);
  const [qrResult, setQrResult] = useState("");
  const [traceResult, setTraceResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Scan for QR code every 500ms
  useEffect(() => {
    let interval;
    if (scanning) {
      interval = setInterval(() => {
        captureAndScan();
      }, 500);
    }
    return () => clearInterval(interval);
    // eslint-disable-next-line
  }, [scanning]);

  const captureAndScan = useCallback(() => {
    if (!webcamRef.current) return;
    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) return;
    // Convert base64 to Uint8ClampedArray
    const img = new window.Image();
    img.src = imageSrc;
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0, img.width, img.height);
      const imageData = ctx.getImageData(0, 0, img.width, img.height);
      const code = jsQR(imageData.data, img.width, img.height);
      if (code && code.data) {
        setQrResult(code.data);
        setScanning(false);
      }
    };
  }, []);

  useEffect(() => {
    if (qrResult) {
      setLoading(true);
      setError("");
      setTraceResult(null);
      let productId = qrResult;
      try {
        // If it's a URL, extract the last part as the product ID
        const url = new URL(qrResult);
        const parts = url.pathname.split('/');
        productId = parts[parts.length - 1];
      } catch (e) {
        // Not a URL, use as is
      }
      getTraceability(productId)
        .then(res => setTraceResult(res.data))
        .catch(err => setError(err.response?.data?.error || "Not found"))
        .finally(() => setLoading(false));
    }
  }, [qrResult]);

  return (
    <Container maxWidth="sm" style={{ marginTop: 32 }}>
      <Typography variant="h4" gutterBottom>Scan Product Label</Typography>
      <Paper style={{ padding: 16, marginBottom: 24 }}>
        {!scanning && (
          <Button variant="contained" color="primary" startIcon={<CameraAltIcon />} onClick={() => { setScanning(true); setQrResult(""); setTraceResult(null); setError(""); }}>
            Start Scanning
          </Button>
        )}
        {scanning && (
          <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Webcam
              audio={false}
              ref={webcamRef}
              screenshotFormat="image/png"
              videoConstraints={videoConstraints}
              style={{ width: '100%', maxWidth: 400, margin: '16px 0', borderRadius: 8 }}
            />
            <Typography variant="body2" color="text.secondary">Point the camera at a QR code...</Typography>
            <Button variant="outlined" color="secondary" onClick={() => setScanning(false)} style={{ marginTop: 16 }}>
              Stop
            </Button>
          </Box>
        )}
        {qrResult && (
          <Alert severity="success" sx={{ mt: 2 }}>QR Code Detected: {qrResult}</Alert>
        )}
        {loading && <CircularProgress sx={{ mt: 2 }} />}
        {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
        {traceResult && traceResult.success && (
          <Box sx={{ mt: 3 }}>
            <Divider sx={{ mb: 2 }} />
            <Typography variant="h6">Product: {traceResult.product.name}</Typography>
            <Typography>Batch: {traceResult.product.batch_number}</Typography>
            <Typography>Category: {traceResult.product.category}</Typography>
            <Typography>Status: {traceResult.product.workflow_status}</Typography>
            <Typography>Manufacturer: {traceResult.product.manufacturer}</Typography>
            <Typography>Expiry: {traceResult.product.expiry_date}</Typography>
          </Box>
        )}
      </Paper>
    </Container>
  );
}

export default Scan; 