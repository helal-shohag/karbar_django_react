import './App.css';
import {Routes, BrowserRouter,Route} from 'react-router-dom' 
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import ProductList from './components/ProductList';
import ProductPage from './pages/ProductPage';
import Category from './components/Category';

function App() {
  return (
    <div className='container-fluid'>
      <Header/>
  <BrowserRouter>
  <Routes>
   <Route path='/' element={<Home/>}/>
  <Route path='/products' element={<ProductList/>}/>
  <Route path='/products/:id' element={<ProductPage/>}/>
  <Route path='/category' element={<Category/>}/>
  </Routes>
  </BrowserRouter>
  <Footer/>
    </div>
  

  );
}

export default App;
