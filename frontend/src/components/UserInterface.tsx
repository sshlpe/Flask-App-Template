import React, {useState, useEffect} from 'react';
import axios from 'axios';
import CardComponent from './CardComponent';

interface User {
    id: number;
    name: string;
    email: string;
}

interface UserInterfaceProps {
    backendName: string;
}

const UserInterface: React.FC<UserInterfaceProps> = ({backendName}) => {

    const api_url = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000';
    const [users, setUsers] = useState<User[]>([]);
    const [newUser, setNewUser] = useState({name:'', email:''});
    const [updateUser, setUpdateUser] = useState({id: '', name: '', email:''});

    const backgroundColors : {[key: string]: string} = {
        flask: 'bg-blue-500',
    };

    const buttonColors : {[key: string]: string} = {
        flask: 'bg-blue-700 hover:bg-blue-600',
    };

    const bgColor = backgroundColors[backendName as keyof typeof backgroundColors] || 'bg-grey-200';
    const btColor = buttonColors[backendName as keyof typeof buttonColors] || 'bg-grey-500 hover:bg-grey-600';

    // fetch users
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(`${api_url}/api/${backendName}/users`);
                setUsers(response.data.reverse());
            } catch (error) {
                console.error('Error fetching data', error);
            }
        }
        fetchData();
    }, [backendName, api_url]);

    const deleteUser = (id: number) => {
        console.log('detete user');
    };

    return (
        <div className={`user-interface ${bgColor} ${backendName} w-full max-w-md p-4 my-4 rounded shadow`}>
            <h2 className='text-xl font-bold text-center text-white mb-6'> 
                {`${backendName}`}
            </h2>
            <div className='space-y-4'>
                {users.map((user) => (
                    <div key={user.id} className='flex items-center justify-between bg-white'>
                        <CardComponent card={user} />
                        <button onClick={() => deleteUser(user.id)} className={`${btColor}`} >
                            detelet user
                        </button>
                    </div>
                   
                ))}
            </div>
        </div>
    );
}

export default UserInterface;