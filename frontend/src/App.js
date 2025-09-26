import './App.css';
import {Routes, BrowserRouter,Route} from 'react-router-dom' 
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import ProductPage from './pages/ProductPage';
import CategoryPage from './pages/CategoryPage';
import CartPage from './pages/CartPage'

function App() {
  return (
    <div className='container-fluid'>
      <Header/>
  <BrowserRouter>
  <Routes>
   <Route path='/' element={<Home/>}/>
  <Route path='/products/:id' element={<ProductPage/>}/>
  <Route path='/categories/:id' element={<CategoryPage/>}/>
  <Route path='/cart/:id' element={<CartPage/>}/>
  </Routes>
  </BrowserRouter>
  <Footer/>
    </div>
  

  );
}

export default App;
