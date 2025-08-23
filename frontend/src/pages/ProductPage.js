import React, { useEffect, useState } from 'react'
import { Link, useParams} from 'react-router-dom'
import {Row,Col} from 'react-bootstrap'

import axios from 'axios'


const ProductPage = () => {
  const { id } = useParams()
const [products, setProducts] = useState({})

useEffect(() => {
  async function fetchProduct() {
    const { data } = await axios.get(`/api/products/${id}`)
    setProducts(data)
  }
  fetchProduct()
}, [id])

return ( 
  <div className='py-5 container '>
    <Link to='/' className='btn btn-light my-3'>Go Back</Link>
    <Row>
      <Col md={6}>
        <img src={products.image} alt={products.name} className='img-fluid'/>
      </Col>
      <Col md={3}>
        <h3>{products.name}</h3>
        <h4>Price: ${products.price}</h4>
        <p>{products.description}</p>
      </Col>
      <Col md={3}>
        <div className='d-flex flex-column border p-3'>
          <Row className='mb-2'>
            <Col>Price:</Col>
            <Col><strong>${products.price}</strong></Col>
          </Row>
          <Row className='mb-2'>
            <Col>Status:</Col>
            <Col>{products.stock > 0 ? 'In Stock' : 'Out of Stock'}</Col>
          </Row>
          <button className='btn btn-dark' type='button' disabled={products.stock === 0}>Add To Cart</button>
        </div>
      </Col>
    </Row>
    
     
  </div>
  )
}

export default ProductPage