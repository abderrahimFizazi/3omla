import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { BiEdit } from 'react-icons/bi';
import { FaTrash } from 'react-icons/fa';

const ListClient = () => {
    const [students, setStudents] = useState([]);

    const studentList = () => {
        
    }

    // const deleteStudent = id => {
    //     api.deleteStudent(id).then(res => {
    //         studentList();
    //         addToast("Student deleted successfully!", { appearance: 'warning' })
    //     }).catch(error => {
    //         console.log(error)
    //     })
    // }

    // useEffect(() => {
    //     studentList();
    // }, [])
    return (<>
        <div className='row'>
            <div className="col-lg-8 mx-auto">
                <Link href="/add-student" className='btn btn-outline-primary my-3' >Add Client
                </Link>
                <table className='table mt-3'>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Address</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {students.map(student => (
                            <React.Fragment key={student.id}>
                                <tr>
                                    <td>{student.id}</td>
                                    <td>{student.name}</td>
                                    <td>{student.email}</td>
                                    <td>{student.address}</td>
                                    <td className='d-flex justify-content-around'>
                                        <Link href={`/student/${student.id}`}>
                                            <div
                                                style={{ 'color': 'blue', 'cursor': 'pointer' }}
                                            >
                                                <BiEdit />
                                            </div>
                                        </Link>
                                        <div
                                            style={{ 'color': 'red', 'cursor': 'pointer' }}
                                            onClick={() => deleteStudent(student.id)}
                                        >
                                            <FaTrash />
                                        </div>
                                    </td>
                                </tr>
                            </React.Fragment>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    </>)
}

export default ListClient