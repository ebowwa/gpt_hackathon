import React from "react";
// import { Layout } from "./layout";
import { Button } from '@/components/ui/button';
import { IconFilm } from 'lucide-react';

// This page is a placeholder for the "Making Your Short" section
const MakingYourShortPage = () => {
  return (
    <Layout>
      <div className="flex flex-col items-center justify-center h-full">
        <IconFilm className="text-6xl text-blue-500 mb-4" />
        <h1 className="text-2xl font-semibold">Making Your Short</h1>
        <p className="text-lg text-gray-600 mt-2">This section is under construction. Check back soon!</p>
        <Button className="mt-4">Go Back</Button>
      </div>
    </Layout>
  );
};

export default MakingYourShortPage;
