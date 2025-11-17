import { useEffect, useState} from 'react'
import { Link, Router, useParams} from 'react-router-dom'
import {Row,Col,ListGroup,ListGroupItem,Button,Card,Form} from 'react-bootstrap'
import { listProductDetail } from '../actions/productActions'
import { useDispatch } from 'react-redux'
import { useSelector } from 'react-redux'
import Loader from '../components/Loader'


const ProductPage = () => {

const [qty,setQty] = useState(1)

const {id} = useParams()
const dispatch = useDispatch()
const productDetails = useSelector(state => state.productDetail)
const {loading,error,product} = productDetails
useEffect(() => {
   dispatch(listProductDetail(id))
}, [dispatch])
console.log(product)

const cartHandler =() =>{
  window.location.href=`/cart/${id}?qty=${qty}`
}

return ( 
  <div className='py-5 container '>
    <Link to='/' className='btn btn-light my-3'>Go Back</Link>
    <Row>
      <Col md={6}>
        <img src={product.image} alt={product.name} className='img-fluid'/>
      </Col>
      <Col md={3}>
        <h3>{product.name}</h3>
        <h4>Price: ${product.price}</h4>
        <p>{product.description}</p>
      </Col>
      <Col md={3}>
        <div className='d-flex flex-column border p-3'>
          <Row className='mb-2'>
            <Col>Price:</Col>
            <Col><strong>${product.price}</strong></Col>
          </Row>
          <Row className='mb-2'>
            <Col>Status:</Col>
            <Col>{product.stock > 0 ? 'In Stock' : 'Out of Stock'}</Col>
          </Row>
          {product.stock > 0 && (
            <ListGroup.Item>
              <Row>
                <Col>Qty</Col>
                <Col>
                <Form>
                  <Form.Control as='select' value={qty} onChange={(e) => setQty(e.target.value)}>
                    {
                     [...Array(product.stock).keys()].map((x) => (
                      <option key={x + 1} value={x + 1}>{x + 1}</option>
                    ))
                    }
                    
                  </Form.Control>
                </Form>
                </Col>
              </Row>
            </ListGroup.Item>
          ) }
          <button className='btn btn-dark' type='button' onClick={cartHandler} disabled={product.stock === 0}>Add To Cart</button>
        </div>
   
      </Col>
    </Row>
       </div>
  )
}

export default ProductPage