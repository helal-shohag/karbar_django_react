import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { Row,Card, Button, Col } from 'react-bootstrap'
import axios from 'axios'

const Category = () => {
    const [categories,setCategories] = useState([])

     useEffect(() =>{
       async function fetchCategory(){
        const {data} = await axios.get('/api/categories/')
        setCategories(data)
       }
       fetchCategory()
     },[])
    
  return (
    <div className='container-fluid mt-5 mb-5'>
       <h2 className='text-center'>Category</h2>
       <Row>
        {categories.map(category =>(
            <Col key={category.id} sm={12} lg={4} md={6} xl={3} className='py-4'>
            <Card className='my-3 p-3 rounded-2xl shadow-lg h-70 hover:mt-4 '>
                <Card.Img src={category.image} alt={category.name} className='pillow rounded'/>
                <Card.Body>
                    <Card.Title>{category.name}</Card.Title>
                    <Card.Text>
                        {category.description}
                    </Card.Text>
                    <Link to={`/categories/${category.id}`}><Button variant='success' className='w-100'>View Products</Button></Link>
                </Card.Body>
            </Card>    
           </Col>         
        ))}
       </Row>
    </div>
  )
}

export default Category