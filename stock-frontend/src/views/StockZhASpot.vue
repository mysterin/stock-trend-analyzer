<template>
  <div>
    <el-form :inline="true" :model="queryParams" class="demo-form-inline">
      <el-form-item label="股票代码">
        <el-input v-model="queryParams.stock_code" placeholder="请输入股票代码" style="width: 120px"></el-input>
      </el-form-item>
      <el-form-item label="数据时间范围">
        <el-date-picker
          v-model="queryParams.date_time_range"
          type="datetimerange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          format="YYYY-MM-DD HH:mm:ss"
          value-format="YYYY-MM-DD HH:mm:ss"
        ></el-date-picker>
      </el-form-item>
      <el-form-item label="量比范围">
        <el-input v-model="queryParams.min_volume_ratio" placeholder="最小量比" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_volume_ratio" placeholder="最大量比" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="最新价范围">
        <el-input v-model="queryParams.min_latest_price" placeholder="最低价" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_latest_price" placeholder="最高价" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="涨跌幅范围">
        <el-input v-model="queryParams.min_change_percentage" placeholder="最小涨跌幅" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_change_percentage" placeholder="最大涨跌幅" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="涨跌额范围">
        <el-input v-model="queryParams.min_change_amount" placeholder="最小涨跌额" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_change_amount" placeholder="最大涨跌额" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="成交量范围">
        <el-input v-model="queryParams.min_volume" placeholder="最小成交量" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_volume" placeholder="最大成交量" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="振幅范围">
        <el-input v-model="queryParams.min_amplitude" placeholder="最小振幅" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_amplitude" placeholder="最大振幅" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="最高价范围">
        <el-input v-model="queryParams.min_highest_price" placeholder="最低最高价" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_highest_price" placeholder="最高最高价" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="最低价范围">
        <el-input v-model="queryParams.min_lowest_price" placeholder="最低最低价" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_lowest_price" placeholder="最高最低价" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="换手率范围">
        <el-input v-model="queryParams.min_turnover_rate" placeholder="最小换手率" style="width: 100px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_turnover_rate" placeholder="最大换手率" style="width: 100px;"></el-input>
      </el-form-item>
      <el-form-item label="5分钟涨跌范围">
        <el-input v-model="queryParams.min_change_5min" placeholder="最小5分钟涨跌" style="width: 120px;"></el-input>
        <span class="wave">~</span>
        <el-input v-model="queryParams.max_change_5min" placeholder="最大5分钟涨跌" style="width: 120px;"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="fetchData">查询</el-button>
        <el-button @click="resetQueryParams">重置</el-button>
      </el-form-item>
    </el-form>

    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="stock_code" label="股票代码" width="120"></el-table-column>
      <el-table-column prop="date_time" label="数据时间" width="180" :formatter="formatDateTime"></el-table-column>
      <el-table-column prop="stock_name" label="股票简称" width="120"></el-table-column>
      <el-table-column prop="latest_price" label="最新价" width="120"></el-table-column>
      <el-table-column prop="change_percentage" label="涨跌幅(%)" width="120"></el-table-column>
      <el-table-column prop="change_amount" label="涨跌额(元)" width="120"></el-table-column>
      <el-table-column prop="volume" label="成交量(手)" width="120"></el-table-column>
      <el-table-column prop="turnover" label="成交额(元)" width="120"></el-table-column>
      <el-table-column prop="amplitude" label="振幅(%)" width="120"></el-table-column>
      <el-table-column prop="highest_price" label="最高价" width="120"></el-table-column>
      <el-table-column prop="lowest_price" label="最低价" width="120"></el-table-column>
      <el-table-column prop="open_price" label="今开价" width="120"></el-table-column>
      <el-table-column prop="previous_close" label="昨收价" width="120"></el-table-column>
      <el-table-column prop="volume_ratio" label="量比" width="120"></el-table-column>
      <el-table-column prop="turnover_rate" label="换手率(%)" width="120"></el-table-column>
      <el-table-column prop="pe_dynamic" label="市盈率-动态" width="120"></el-table-column>
      <el-table-column prop="pb" label="市净率" width="120"></el-table-column>
      <el-table-column prop="total_market_value" label="总市值(元)" width="120"></el-table-column>
      <el-table-column prop="circulating_market_value" label="流通市值(元)" width="120"></el-table-column>
      <el-table-column prop="increase_speed" label="涨速" width="120"></el-table-column>
      <el-table-column prop="change_5min" label="5分钟涨跌(%)" width="120"></el-table-column>
      <el-table-column prop="change_60d" label="60日涨跌幅(%)" width="120"></el-table-column>
      <el-table-column prop="change_ytd" label="年初至今涨跌幅(%)" width="120"></el-table-column>
    </el-table>

    <el-pagination
      background
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
      :page-size="queryParams.page_size"
      :current-page="queryParams.page_num"
      :page-sizes="[20, 50, 100, 200]"
      @current-change="handlePageChange"
      @size-change="handleSizeChange">
    </el-pagination>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import { spotList } from '@/api/stockZhASpot'
import dayjs from 'dayjs'

export default {
  name: 'StockZhASpot',
  setup() {
    const tableData = ref([])
    const total = ref(0)
    const defaultQueryParams = {
      stock_code: '',
      date_time_range: [],
      min_volume_ratio: '',
      max_volume_ratio: '',
      min_latest_price: '',
      max_latest_price: '',
      min_change_percentage: '',
      max_change_percentage: '',
      min_change_amount: '',
      max_change_amount: '',
      min_volume: '',
      max_volume: '',
      min_amplitude: '',
      max_amplitude: '',
      min_highest_price: '',
      max_highest_price: '',
      min_lowest_price: '',
      max_lowest_price: '',
      min_turnover_rate: '',
      max_turnover_rate: '',
      min_change_5min: '',
      max_change_5min: '',
      page_num: 1,
      page_size: 20,
      order_by: 'date_time',
      order_type: 'desc'
    }
    const queryParams = reactive({ ...defaultQueryParams })

    const fetchData = async () => {
      try {
        const response = await spotList(queryParams)
        console.log('response:', response) // 调试信息
        tableData.value = response.list
        total.value = response.total
      } catch (error) {
        console.error('请求失败:', error)
      }
    }

    const handlePageChange = (page) => {
      queryParams.page_num = page
      fetchData()
    }

    const handleSizeChange = (size) => {
      queryParams.page_size = size
      fetchData()
    }

    const resetQueryParams = () => {
      Object.assign(queryParams, defaultQueryParams)
    }

    const formatDateTime = (row, column, cellValue) => {
      return dayjs(cellValue).format('YYYY-MM-DD HH:mm:ss')
    }

    onMounted(() => {
      fetchData()
    })

    return {
      tableData,
      total,
      queryParams,
      fetchData,
      handlePageChange,
      handleSizeChange,
      resetQueryParams,
      formatDateTime
    }
  }
}
</script>

<style>
.wave {
  margin: 0 10px;
}
</style>