import React, { useEffect, useState } from 'react'
import {  Link,  Router,  useParams} from 'react-router-dom'
import {Row,Col, ListGroup, FormControl} from 'react-bootstrap'

import axios from 'axios'


const ProductPage = () => {
  const [qty,setQuantity] =useState(1 )
  const { id } = useParams()
const [products, setProducts] = useState([])

useEffect(() => {
  async function fetchProduct() {
    const { data } = await axios.get(`/api/products/${id}`)
    setProducts(data)
  }
  fetchProduct()
}, [id])

const addToCart =() =>{
   
  console.log('Add To cart ', {id})
}
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
          {products.stock> 0 && (
          <ListGroup>
           <Row>
            <Col className='mt-2'>Quantity :</Col>
            <Col xs='auto' className='my-1 '>
            <FormControl value={qty} as="Select" onChange={(e)=>setQuantity(e.target.value)}>
             {[...Array(products.stock).keys()].map((x)=>
                <option value={x+1}>
                  {x+1}
                </option>
              )}
            </FormControl>
            </Col>
           </Row>
          </ListGroup>
          )
          
          }
          <Link to={`/cart/${products._id}`}><button className='btn btn-dark' onClick={addToCart} type='button' disabled={products.stock === 0}>Add To Cart</button></Link>
        </div>
      </Col>
    </Row>
    
     
  </div>
  )
}

export default ProductPage