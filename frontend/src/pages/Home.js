import React from 'react'
import { Row,Col } from 'react-bootstrap'
import ProductList from '../components/ProductList'
import SliderShow from '../components/SliderShow'
import axios from 'axios'
import { useState,useEffect } from 'react'
import Category from '../components/Category'




function Home() {
  const [products,setProducts] = useState([])

  useEffect(()=>{
    async function fetchProducts(){
      const {data} = await axios.get('/api/products/')
      setProducts(data)
    } 
    fetchProducts()
  },[])
  return (
    <div>
      <SliderShow/>
      <Category />
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