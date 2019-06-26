import Vue from 'vue';
import VueRouter from 'vue-router';
import Favorite from '@/components/Favorite.vue';
import Index from '@/components/Index.vue';
import Audit from '@/components/Audit.vue';
import FavoriteCard from '@/components/FavoriteCard.vue';
import Category from '@/components/Category.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  // base: '/',
  routes: [
    {
      path: '/favorite',
      name: 'Favorite',
      component: Favorite,
    },
    {
      path: '/',
      name: 'index',
      component: Index,
    },
    {
      path: '/audit',
      name: 'Audit',
      component: Audit,
    },
    {
      path: '/favorite-cards',
      name: 'FavoriteCard',
      component: FavoriteCard,
    },
    {
      path: '/categories',
      name: 'Category',
      component: Category,
    },
  ],
});
