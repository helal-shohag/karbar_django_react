import React, { useState } from 'react'
import {Form,Button,Col,Row} from 'react-bootstrap'
import { Link } from 'react-router-dom';
import FromContainer from '../components/FromContainer'
function Login() {
  const [email,setEmail] = useState('')
  const [password,setPassword] = useState('')

    const handleSubmit= (e) =>{
        e.preventDefault(
          email,password
        );
        console.log('submitted')
    }
  return (
    <FromContainer>
        <h2>Login</h2>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId='email'>
            <Form.Label>Email Address</Form.Label>
            <Form.Control type='email' placeholder='Enter email' value={email} onChange={(e) => setEmail(e.target.value)} ></Form.Control>
          </Form.Group>

          <Form.Group controlId='password'>
            <Form.Label >Password</Form.Label>
            <Form.Control type='password' placeholder='Enter password' value={password} onChange={(e) => setPassword(e.target.value)} ></Form.Control>
          </Form.Group>
         <Row className='py-3'>
          <Col>
            New Customer? <Link to='/register'>Register</Link>
          </Col>
         </Row>
         <Button type='submit' variant='primary' className='mt-4 mb-4' onClick={handleSubmit}>Submit</Button>
         
        </Form>
    </FromContainer>
  )
}

export default Login