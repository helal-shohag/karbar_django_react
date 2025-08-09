import React from 'react'
import { Card,Button } from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'

const ProductList = ({product}) => {
  return (
    <Card className='my-3 p-3 rounded-xl shadow-lg'>
     <Link to={`/products/${product.id}`} className='text-center'>
     <Card.Img src={product.image}/>
     <Card.Body>
        <Card.Title py>
            {product.name}<br/>
        </Card.Title>
        <Card.Text>
           <Rating value={product.rating} review={product.review}/>
            
        </Card.Text>
        <Card.Text>
            {product.category}
            
        </Card.Text>
        <Card.Text>
            {product.description}
            
        </Card.Text>
     </Card.Body>
     </Link>
    <Button className=''>Add To Cart</Button>
     
    </Card>
  )
}

export default ProductList