import axios from "axios";
const API_BASE = "http://localhost:5000/api";

export const getProducts = (params) => axios.get(`${API_BASE}/products`, { params });
export const getProduct = (id) => axios.get(`${API_BASE}/products/${id}`);
export const createProduct = (data) => axios.post(`${API_BASE}/products`, data);
export const updateProduct = (id, data) => axios.put(`${API_BASE}/products/${id}`, data);
export const deleteProduct = (id) => axios.delete(`${API_BASE}/products/${id}`);

export const createQualityCheck = (productId, data) =>
  axios.post(`${API_BASE}/products/${productId}/quality-checks`, data);

export const runAutoQualityChecks = (productId) =>
  axios.post(`${API_BASE}/products/${productId}/quality-checks/auto`);

export const createLabel = (productId, data) =>
  axios.post(`${API_BASE}/products/${productId}/labels`, data);

export const autoGenerateLabels = (productId) =>
  axios.post(`${API_BASE}/products/${productId}/labels/auto`);

export const runProductWorkflow = (productId) =>
  axios.post(`${API_BASE}/products/${productId}/workflow/run`);

export const runBatchWorkflow = (productIds) =>
  axios.post(`${API_BASE}/batch/workflow/run`, { product_ids: productIds });

export const generateBatchLabels = (productIds, labelType = "qr_code") =>
  axios.post(`${API_BASE}/batch/labels/generate`, { product_ids: productIds, label_type: labelType });

export const printLabel = (labelId) =>
  axios.post(`${API_BASE}/labels/${labelId}/print`);

export const verifyLabel = (labelId) =>
  axios.post(`${API_BASE}/labels/${labelId}/verify`);

export const getTraceability = (identifier) =>
  axios.get(`${API_BASE}/traceability/${identifier}`);

export const getAnalyticsDashboard = () =>
  axios.get(`${API_BASE}/analytics/dashboard`);

export const getQualityTrends = (days = 30) =>
  axios.get(`${API_BASE}/analytics/quality-trends`, { params: { days } });

export const getCategoryBreakdown = () =>
  axios.get(`${API_BASE}/analytics/category-breakdown`);

export const getIndianProductQualityParameters = (productKey) =>
  axios.get(`${API_BASE}/indian-products/parameters/${productKey}`);

export const clearAutoQualityChecks = (productId) =>
  axios.delete(`${API_BASE}/products/${productId}/quality-checks/auto`);

export const clearAutoLabels = (productId) =>
  axios.delete(`${API_BASE}/products/${productId}/labels/auto`);
