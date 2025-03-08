<template>
  <div class="dashboard">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card>
          <h3>股票趋势分析</h3>
          <p>查看和分析股票的历史趋势和未来预测。</p>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <h3>实时数据</h3>
          <p>获取最新的股票市场数据和动态。</p>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card>
          <h3>投资组合管理</h3>
          <p>管理和优化你的股票投资组合。</p>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'StockDashboard'
}
</script>

<style scoped>
.dashboard {
  padding: 20px;
}
.el-card {
  text-align: center;
}
</style>