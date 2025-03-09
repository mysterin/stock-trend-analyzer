import axios from 'axios'
import { ElMessage } from 'element-plus'

// 创建 axios 实例
const service = axios.create({
  baseURL: '/api', // 请求路径前缀
  timeout: 10000, // 请求超时 10s
  headers: {
    'Content-Type': 'application/json' // 请求体格式为 JSON
  }
})

// 递归函数遍历对象并删除空字符串字段
function removeEmptyStrings(obj) {
  for (const key in obj) {
    if (typeof obj[key] === 'object' && obj[key] !== null) {
      removeEmptyStrings(obj[key])
    } else if (obj[key] === '') {
      delete obj[key]
    }
  }
}

// 请求拦截器
service.interceptors.request.use(
  config => {
    // 生成豪秒级时间戳作为请求 id
    const requestId = Date.now()
    if (config.method === 'post' || config.method === 'put') {
      if (config.data) {
        config.data.id = requestId
        // 遍历请求体中的字段，删除空字符串字段
        removeEmptyStrings(config.data)
      } else {
        config.data = { id: requestId }
      }
    }
    return config
  },
  error => {
    // 处理请求错误
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  response => {
    const res = response.data
    // 如果 code 不为 0，提示错误信息
    if (res.code !== 0) {
      ElMessage.error(res.msg || 'Error')
      return Promise.reject(new Error(res.msg || 'Error'))
    } else {
      return res.data
    }
  },
  error => {
    // 处理响应错误
    ElMessage.error(error.message || '请求失败')
    return Promise.reject(error)
  }
)

export default service