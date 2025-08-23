import React, { useState,useEffect} from 'react'
import { Link,useParams } from 'react-router-dom'
import { Row, Card, Col } from 'react-bootstrap'
import axios from 'axios'


const CategoryPage = () => {
    const [categoryPage,setCategoryPage] = useState([])
    const { id } = useParams()

    useEffect(() =>{
       async function fetchCategoryPage(){
        const {data} = await axios.get(`/api/categories/${id}`)
        setCategoryPage(data)
       }
       fetchCategoryPage()
     },[id])
  return (
    <div className='container-fluid mt-5 mb-5'>
         <h2 className='text-center'>Category</h2>
        <Link to='/'><h2 className='btn btn-light mb-4'>Go Back</h2></Link>
        
         <Row>
               <Col md={6}>
                 <img src={categoryPage.image} alt={categoryPage.name} className='img-fluid'/>
               </Col>
               <Col md={6}>
                 <h3>{categoryPage.name}</h3>
                 
                 <p>{categoryPage.description}</p>
               </Col>
               
             </Row>
    </div>
  )
}

export default CategoryPage