/**
 * v0 by Vercel.
 * @see https://v0.dev/t/y1X9ynZA18I
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Component() {
  return (
    <main className="flex flex-col items-center justify-center h-screen px-4 py-12 bg-gray-100 dark:bg-gray-900">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100">
          YouTube-short-inator
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          Create the perfect YouTube Short in an instant, with the power of AI
        </p>
      </div>
      <div className="flex w-full max-w-md items-center space-x-2 mt-8">
        <Input placeholder="Enter your prompt here" type="text" />
        <Link href="/result">
          <Button type="submit">Submit</Button>
        </Link>
      </div>
    </main>
  );
}
