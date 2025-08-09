
import React from 'react'
import Slider from 'react-slick'

import image_1 from '../Assets/slider1.jpg'
import image_2 from '../Assets/slider2.png'
import image_3 from '../Assets/slider3.jpg'


const SliderShow = () => {
    var settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    autoplay:true,
    slidesToScroll: 1
  };
  return (
    
    <div className='container'>
       <Slider {...settings}>
     
            <div >
          <img src={image_1 } alt='product' className='w-100 h-20 rounded mt-4 shadow-lg'  />
            </div>
            <div>
                <img src={image_2} className='w-100 h-20'/>
            </div>
            <div>
                <img src={image_3} className='w-100 h-20'/>
            </div>
        </Slider> 
    </div>
  )
}

export default SliderShow