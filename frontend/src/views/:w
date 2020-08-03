import axios from "axios";
import store from "@/store";

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/v1/',
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
  },
})

// 共通前処理 
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access')
    if (token) {
      config.headers.Authorization = `JWT ${token}`;
      console.log(config); // DEBUG 
      return config
    }
  return config
}, function (error) {
  return Promise.reject(error)
})

export default api
