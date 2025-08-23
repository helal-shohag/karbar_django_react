import React from 'react'
import { Card,Button,Col} from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'

const ProductList = ({product}) => {
  return (
    <Col key={product.id}>
            <Card className='my-3 p-3 rounded-2xl shadow-lg'>
                <Card.Img src={product.image} alt={product.name} className='h-100 w-300 object-fit'/>
                <Card.Body>
                    <Card.Title>{product.name}</Card.Title>
                    <Card.Text>
                        {product.description}
                    </Card.Text>
                    <Link to={`/products/${product._id}`}><Button variant='success' className='w-100 mb-4'>Add To Cart</Button></Link>
                    <Link to={`/products/${product._id}`}><Button variant='success' className='w-100'>View Product</Button></Link>
                </Card.Body>
            </Card>    
           </Col>         
  )
}

export default ProductList