import React, { Children } from 'react'
import {Container,Col,Row} from 'react-bootstrap'

function FromContainer({children}) {
  return (
    <div>
        <Container>
            <Row className='justify-content-md-center mt-5'>
                <Col xs={12} md={6} >
                {children}
                </Col>
            </Row>
        </Container>
    </div>
  )
}

export default FromContainer