import React from 'react'
import { useEffect } from 'react'
import { Link,} from 'react-router-dom'
import { useDispatch,useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { addToCart } from '../actions/CartActions'
import { Row,Col,ListGroup,Image,Form,Button,Card } from 'react-bootstrap'
import Message from '../components/Messege'


function CartPage() {
  const {id} = useParams()
  const dispatch = useDispatch()

  const productId  = id
  const qty = window.location.search ? Number(window.location.search.split('=')[1]) : 1

  useEffect(() => {
    if(productId){
      dispatch(addToCart(productId,qty))
    }else{
      
    }
  },[dispatch,productId,qty])

  const cart = useSelector(state  => state.cart)
  const {cartItems} = cart
  
  return (
   <Row>
    <Col md={8}>
      <h2>Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <Message variant='info'>
          Your cart is empty <Link to='/'>Go Back</Link>
        </Message>
      ) :(
        <ListGroup variant='flush'>
          {cartItems.map(item => (
            <ListGroup.Item key={item.product}>
              <Row>
                <Col md={2}>
                <Image src={item.image} alt={item.name} fluid rounded/>
                </Col>
                <Col md={3}>
                  <Link to={`/product/${item.product}`}>{item.name}</Link>
                </Col>
              </Row>
            </ListGroup.Item>
          ))}
        </ListGroup>
      )}
    </Col>

    <Col md={4}>
    </Col>
   </Row>
  )
}

export default CartPage