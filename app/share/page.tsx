import React from "react";
// import { Layout } from "./layout";
import { Button } from '@/components/ui/button';
import { IconShare2 } from 'lucide-react';

// This page provides a simple interface for sharing content
const SharePage = () => {
  return (
    <Layout>
      <div className="flex flex-col items-center justify-center h-full p-4">
        <IconShare2 className="text-6xl text-purple-500 mb-4" />
        <h1 className="text-2xl font-semibold">Share With Your Friends</h1>
        <p className="text-lg text-gray-600 mt-2">Spread the word and share your experience!</p>
        <Button className="mt-4">Share Now</Button>
      </div>
    </Layout>
  );
};

export default SharePage;
