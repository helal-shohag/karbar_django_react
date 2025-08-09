import React from 'react'
import { Row,Col } from 'react-bootstrap'
import products from '../Assets/products'
import ProductList from '../components/ProductList'
import SliderShow from '../components/SliderShow'
import axios from 'axios'
import { useState,useEffect } from 'react'




function Home() {
  const [products,setProducts] = useState([])

  useEffect(()=>{
    async function fetchProducts(){
      const {data} = await axios.get('http://127.0.0.1:8000/api/products/')
      setProducts(data)
    } 
    fetchProducts()
  },[])
  return (
    <div>
      <SliderShow/>
        <h2 className='text-center mt-4 mb-4 '>Latest Products</h2>
        <Row>
           {products.map(product=>(
            <Col key={product.id} sm={12} lg={4} md={6} xl={3}>
            <ProductList product={product}/>
            
            </Col>
           ))}
        </Row>
    </div>
  )
}

export default Home