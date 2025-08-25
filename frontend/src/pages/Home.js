import React from 'react'
import { Row,Col } from 'react-bootstrap'
import ProductList from '../components/ProductList'
import SliderShow from '../components/SliderShow'

import { useEffect } from 'react'
import Category from '../components/Category'
import  {useDispatch,useSelector} from 'react-redux'
import { listProduct } from '../actions/productActions'



function Home() {
  const dispatch = useDispatch()
  const productList = useSelector(state => state.productListReducers)
  useEffect(()=>{
    dispatch(listProduct())
  },)
   const {Products} = productList
  
  return (
    <div>
      <SliderShow/>
      <Category />
        <h2 className='text-center mt-4 mb-4 '>Latest Products</h2>
        <Row>
           {Products.map(product=>(
            <Col key={product.id} sm={12} lg={4} md={6} xl={3}>
            <ProductList product={product}/>
            </Col>
           ))}
        </Row>
      
    </div>
  )
}

export default Home