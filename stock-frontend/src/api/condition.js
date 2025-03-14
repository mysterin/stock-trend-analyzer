import request from '@/utils/request'

// 新增或更新查询条件
export async function saveCondition(data) {
  return request({
    url: '/api/condition/save',
    method: 'post',
    data
  })
}

// 分页查询查询条件
export async function listConditions(params) {
  return request({
    url: '/api/condition/list',
    method: 'post',
    data: params
  })
}

// 删除查询条件
export async function deleteCondition(query_condition_id) {
  return request({
    url: '/api/condition/delete',
    method: 'post',
    data: { query_condition_id }
  })
}