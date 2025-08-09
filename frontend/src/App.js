import './App.css';
import {Routes, BrowserRouter,Route} from 'react-router-dom' 
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import ProductList from './components/ProductList';
import ProductPage from './pages/ProductPage';

function App() {
  return (
    <div className='container-fluid'>
      <Header/>
      <BrowserRouter>
  <Routes>
   <Route path='/' element={<Home/>}/>
  <Route path='/product' element={<ProductList/>}/>
   <Route path='/products/:id' element={<ProductPage/>}/>
  
  </Routes>
  </BrowserRouter>
  <Footer/>
    </div>
  

  );
}

export default App;
