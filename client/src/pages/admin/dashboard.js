import React from 'react';
import Sidebar from '@/components/admin/Sidebar';
import ListClient from '../../components/client/listClient';
const Home = () => {
  return (
    <>
      <Sidebar/>
      <ListClient/>
    </>
  );
};

export default Home;
