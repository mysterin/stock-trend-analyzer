import request from '@/utils/request'

// 获取 A 股实时行情数据
export async function spotList(data) {
  return request({
    url: '/stocks/spot/list',
    method: 'post',
    data
  })
}