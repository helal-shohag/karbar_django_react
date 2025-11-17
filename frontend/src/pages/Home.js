import React from 'react'
import { Row,Col } from 'react-bootstrap'
import ProductList from '../components/ProductList'
import SliderShow from '../components/SliderShow'
import Loader from '../components/Loader'
import { useEffect } from 'react'
import Category from '../components/Category'
import  {useDispatch,useSelector} from 'react-redux'
import { listProduct } from '../actions/productActions'



function Home() {
  const dispatch = useDispatch()
  const productList = useSelector(state => state.productList)
  const {error,loading,products} = productList
  useEffect(() =>{
    dispatch(listProduct())
  },[dispatch])

 
  return (
    <div>
      <SliderShow/>
      <Category />
       <h2 className='text-center mt-4 mb-4 '>Latest Products</h2>
      { products ? 
      <Row>
           {products.map(product=>(
            <Col key={product.id} sm={12} lg={4} md={6} xl={3}>
            <ProductList product={product}/>
            </Col>
           ))}
        </Row> :loading ? <Loader/> : error}
      
       

    </div>
  )
}

export default Home