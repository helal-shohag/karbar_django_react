import React, { useEffect, useState } from 'react'
import { Link, useParams} from 'react-router-dom'
import {Row,Col} from 'react-bootstrap'
import products from '../Assets/products'
import axios from 'axios'


const ProductPage = () => {
  const { id } = useParams()
const [product, setProduct] = useState({})

useEffect(() => {
  async function fetchProduct() {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/products/${id}`)
    setProduct(data)
  }
  fetchProduct()
}, [id])

return (
  <div>
    <h2 className='py-4'> {product.name}</h2>

  </div>
  )
}

export default ProductPage