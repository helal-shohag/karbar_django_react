import React from 'react'
import { FaRegStar } from "react-icons/fa6";



const Rating = ({value,review}) => {
  return (
    <div>
        {value + 'of' + review +'reviews'} <br/>
        <FaRegStar/>
    </div>
  )
}

export default Rating