<template>
  <el-container style="height: 100vh;">
    <el-aside width="200px">
      <el-menu :default-active="activeMenu" @select="handleSelect">
        <template v-for="route in menuRoutes">
          <el-menu-item
            v-if="!route.children"
            :key="route.path"
            :index="route.path"
          >
            {{ route.meta.title }}
          </el-menu-item>
          <el-sub-menu v-else :key="`submenu-${route.path}`" :index="route.path">
            <template #title>{{ route.meta.title }}</template>
            <el-menu-item
              v-for="child in route.children"
              :key="child.path"
              :index="`${route.path}/${child.path}`"
            >
              {{ child.meta.title }}
            </el-menu-item>
          </el-sub-menu>
        </template>
      </el-menu>
    </el-aside>
    <el-container>
      <el-header class="header-with-divider">{{ headerTitle }}</el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  data() {
    return {
      activeMenu: '/dashboard'
    }
  },
  setup() {
    const router = useRouter()
    const route = useRoute()
    const menuRoutes = computed(() => {
      return router.options.routes[0].children
    })

    const headerTitle = computed(() => {
      const pathSegments = route.path.split('/').filter(segment => segment)
      const titles = []
      let currentRoutes = router.options.routes[0].children

      for (const segment of pathSegments) {
        const currentRoute = currentRoutes.find(r => r.path === segment)
        if (currentRoute) {
          titles.push(currentRoute.meta.title)
          if (currentRoute.children) {
            currentRoutes = currentRoute.children
          } else {
            break
          }
        }
      }

      return titles.join(' / ')
    })

    return {
      menuRoutes,
      headerTitle
    }
  },
  methods: {
    handleSelect(key) {
      // 确保 key 是绝对路径
      if (!key.startsWith('/')) {
        key = '/' + key
      }
      // 查找选中的路由
      const selectedRoute = this.findRouteByPath(this.menuRoutes, key)
      // 如果路由有 redirect 属性，导航到重定向的路径
      if (selectedRoute && selectedRoute.redirect) {
        this.$router.push({ path: selectedRoute.redirect })
      } else {
        this.$router.push({ path: key })
      }
    },
    findRouteByPath(routes, path) {
      for (const route of routes) {
        if (route.path === path) {
          return route
        }
        if (route.children) {
          const childRoute = this.findRouteByPath(route.children, path)
          if (childRoute) {
            return childRoute
          }
        }
      }
      return null
    }
  }
}
</script>

<style>
.header-with-divider {
  border-bottom: 1px solid #dcdfe6; /* 分界线的颜色 */
}
</style>