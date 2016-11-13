import VueRouter from 'vue-router';
import Main from './pages/Main';
import Home from './pages/Home';
import Recipes from './pages/Recipes';
import RecipeFavorites from './pages/RecipeFavorites';
import RecipeDetail from './pages/RecipeDetail';
import RecipeCreate from './pages/RecipeCreate';
import UserDetail from './pages/UserDetail';
import UserRecipes from './pages/UserRecipes';
import UserFavorites from './pages/UserFavorites';
import UserFollowers from './pages/UserFollowers';
import Login from './pages/Login';
import Register from './pages/Register';
import NotFound from './pages/NotFound';


const routes = [
  { path: '/', component: Main,
    children: [
      { path: '', component: Home, name: 'home' },
      { path: 'recipes', component: Recipes, name: 'recipe-list' },
      { path: 'recipes/favorites', component: RecipeFavorites, name: 'recipe-favorites' },
      { path: 'recipes/create', component: RecipeCreate, name: 'recipe-create' },
      { path: 'recipes/:recipeId', component: RecipeDetail, name: 'recipe-detail' },
      { path: 'user/:userId', component: UserDetail, name: 'user-detail-root',
        children: [
          { path: '', component: UserRecipes, name: 'user-detail' },
          { path: 'favorites', component: UserFavorites, name: 'user-favorites' },
          { path: 'followers', component: UserFollowers, name: 'user-followers' },
        ],
      },
    ],
  },
  { path: '/login', component: Login, name: 'login' },
  { path: '/register', component: Register, name: 'register' },
  { path: '*', component: NotFound, name: 'not-found' },
];

const router = new VueRouter({
  routes,
  mode: 'history',
});

export default router;
